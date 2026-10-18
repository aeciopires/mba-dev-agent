from google.adk.agents import Agent
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.tool_context import ToolContext


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


def get_invoice_by_client_id(client_id: int | str) -> dict:
    """Retorna a fatura correspondente ao ID fornecido."""
    normalized_client_id = str(client_id)
    for invoice in INVOICES:
        if str(invoice["client_id"]) == normalized_client_id:
            return invoice
    return {"error": "Fatura não encontrada."}


def cancel_plan(client_id: str, password: str, tool_context: ToolContext) -> dict:
    """Cancela o plano do cliente correspondente ao ID fornecido."""
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


root_agent = Agent(
    name="meu_agente2",
    instruction="""
        Você é o atendente de conta interativo da Acme LTDA.
        Você é o responsável por:
         - Informar ao cliente sobre sua assinatura: o plano, status e renovação.
         - Tirar dúvidas sobre as faturas do cliente.
         - Cancelar a assinatura do cliente, se solicitado.
        O usuário precisa fornecer o ID do cliente para que você possa buscar as informações corretas.
        Seja cordial e direto.
    """,
    model="gemini-2.5-flash",
    tools=[
        FunctionTool(get_invoice_by_client_id),
        FunctionTool(cancel_plan, require_confirmation=True),
    ],
)
