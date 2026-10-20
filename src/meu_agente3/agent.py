"""
    Module contendo a definição do agente principal e dos sub-agentes para
      gerenciamento de faturas e planos de assinatura.
"""
import random

from google.adk.agents import Agent
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.tool_context import ToolContext

#----------------------------------
# Variables
#----------------------------------

INVOICES = [
    {
        "id": "fatura_0001",
        "client_id": 45678,
        "invoice": 100.00,
        "expired_date": "2024-06-30",
        "generated_date": "2024-06-01",
        "status": "pending",
    },
    {
        "id": "fatura_0002",
        "client_id": 35678,
        "invoice": 200.00,
        "expired_date": "2024-07-30",
        "generated_date": "2024-07-01",
        "status": "paid",
    },
]

PLANS: dict[str, dict] = {
    "client_45678": {
        "plan": "Premium",
        "status": "activated",
        "renovation": "2024-07-01",
    },
    "client_35678": {
        "plan": "Basic",
        "status": "activated",
        "renovation": "2024-08-01",
    },
}

#----------------------------------
# Tools
#----------------------------------

def get_invoice_by_client_id(client_id: int | str) -> dict:
    """
        Retorna a fatura correspondente ao ID fornecido.
        Args:
            client_id (int | str): O ID do cliente para o qual a fatura deve ser buscada.
        Returns:
            dict: Um dicionário contendo os detalhes da fatura, ou uma mensagem de erro
              se a fatura não for encontrada.
    """
    # Simulação de um erro de conexão com o banco de dados
    return {"error": "DB Connection Error: Unable to fetch faturas from the database."}

    #normalized_client_id = str(client_id)
    #for invoice in INVOICES:
    #    if str(invoice["client_id"]) == normalized_client_id:
    #        return invoice
    #return {"error": "Fatura não encontrada."}


def cancel_plan(client_id: str, password: str, tool_context: ToolContext) -> dict:
    """
        Cancela o plano do cliente correspondente ao ID fornecido.
        Args:
            client_id (str): O ID do cliente para o qual o plano deve ser cancelado.
            password (str): A senha para confirmar a ação.
            tool_context (ToolContext): O contexto da ferramenta.
        Returns:
            dict: Um dicionário contendo a mensagem de resultado e o status da operação.
    """

    if tool_context.tool_confirmation is None:
        tool_context.request_confirmation(
            hint="Tem certeza de que deseja cancelar?",
            payload={
                "client_id": client_id,
                "senha": ""
            }
        )
        return {"status": "aguardando_confirmacao"}

    if not tool_context.tool_confirmation.confirmed:
        return {"status": "nao_cancelada", "mensagem": "Cancelamento não confirmado pelo usuário."}

    if password != "senha123":
        return {
            "message": "Senha incorreta. O plano não pode ser cancelado.",
            "status": "not_cancelled",
        }

    plan = PLANS.get(f"client_{client_id}")
    if plan is not None:
        plan["status"] = "cancelled"
    return {
        "message": f"O plano do cliente {client_id} foi cancelado com sucesso.",
        "status": "cancelled",
    }


def get_status_subagent() -> dict:
    """
        Retorna o status da empresa ACME, simulando diferentes estados de operação.
        Returns:
            dict: Um dicionário contendo o status e uma mensagem informativa.
    """
    status = random.choice(["operational", "maintenance", "offline"])
    return {"status": status, "message": f"A empresa ACME está atualmente com o status: {status}."}


#----------------------------------
# Sub-agents
#----------------------------------

consultor_fatura_subagent = Agent(
    name="consultor_bills",
    description="Especialista responsável por listar as faturas de um cliente especifico.",
    instruction="""
        Você é um consultor de faturas da Acme LTDA.
        Você é responsável por:
         - Informar ao cliente sobre suas faturas: status, vencimento e valor.
        O usuário precisa fornecer o ID do cliente para que você possa buscar as informações corretas.
        Seja cordial e direto.
    """,
    model="gemini-2.5-flash",
    tools=[
        FunctionTool(get_invoice_by_client_id),
    ],
    # Impede que o sub-agente transfira a conversa para outros agentes,
    # mantendo o controle da interação.
    disallow_transfer_to_peers=True,
)


consultor_plan_subagent = Agent(
    name="consultor_plan",
    description="""
        Especialista responsável por fornecer ao cliente informações sobre o plano de assinatura.
    """,
    instruction="""
        Você é um consultor de planos de assinaturas da Acme LTDA.
        Você é responsável por:
         - Informar ao cliente sobre sua assinatura: o plano, status e renovação.
        O usuário precisa fornecer o ID do cliente para que você possa buscar as informações corretas.
        O usuário também pode solicitar o cancelamento do plano, para isso você deve solicitar a senha do cliente e confirmar a ação.
        Seja cordial e direto.
    """,
    model="gemini-2.5-flash",
    tools=[
        FunctionTool(cancel_plan, require_confirmation=True),
    ],
    # Impede que o sub-agente transfira a conversa para outros agentes,
    # mantendo o controle da interação.
    disallow_transfer_to_peers=True,
)


status_subagent = Agent(
    name="status_subagent",
    description="""
        Sub-agente responsável por fornecer o status de outros sub-agentes.
    """,
    instruction="""
        Você é um sub-agente de status da Acme LTDA.
        Você é responsável por:
         - Informar ao cliente sobre o status de outros sub-agentes.
        O coordenador precisa fornecer o nome do sub-agente para que você possa buscar as informações corretas.
        Seja cordial e direto.
    """,
    model="gemini-2.5-flash",
    tools=[
        FunctionTool(get_status_subagent),
    ],
    # Este sub-agente não mantém contexto entre interações
    # Evita um loop de chamadas entre sub-agentes, garantindo que cada solicitação
    # seja tratada de forma independente.
    mode="single_turn",
    # Impede que o sub-agente transfira a conversa para outros agentes,
    # mantendo o controle da interação.
    disallow_transfer_to_peers=True,
)

#----------------------------------
# Coordinator Agent
#----------------------------------
root_agent = Agent(
    name="operator_billing",
    description="""
        Agente responsável por ajudar o cliente a gerenciar sua conta, incluindo faturas e planos de assinatura.
    """,
    instruction="""
        Você é o atendente de conta interativo da Acme LTDA.
        Quando algum subagente retornar um erro de sistema, 
        use o subagente `status_subagent` para verificar se os serviços da Acme estão operacionais, em manutenção ou offline.
        Caso os serviços estejam offline ou em manutenção, informe ao usuário que 
        os serviços da Acme estão temporariamente indisponíveis e que ele deve tentar novamente mais tarde.
        Caso os serviços estejam operacionais, informe ao usuário que houve um erro de sistema e que ele deve tentar novamente mais tarde.
        O que são erros de sistema? 
        São erros que não são causados por bugs, erros de comunicação com sistemas externos, 
        como banco de dados, APIs de terceiros, etc. Esses erros podem ser temporários.
        Não informe ao usuário detalhes técnicos sobre o erro de sistema, apenas informe que houve um erro de sistema e que ele deve tentar novamente mais tarde.
        Seja cordial e direto.
    """,
    model="gemini-2.5-flash",
    sub_agents=[
        consultor_fatura_subagent,
        consultor_plan_subagent,
        status_subagent,
    ],
)
