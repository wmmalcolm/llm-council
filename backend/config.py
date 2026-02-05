# Council members - list of OpenRouter model identifiers
# These correspond to your "Board of Directors" models.
COUNCIL_MODELS = [
    # ChatGPT / OpenAI
    "openai/gpt-5.1",

    # Gemini (Google)
    "google/gemini-3-pro-preview",

    # Claude (Anthropic)
    "anthropic/claude-sonnet-4.5",

    # Grok (xAI)
    "x-ai/grok-4",

    # Perplexity (placeholder – confirm exact model id in OpenRouter)
    "perplexity/sonar-pro",  # TODO: check OpenRouter docs for correct id

    # Copilot (placeholder – only if exposed via OpenRouter)
    "github/copilot-gpt-4o",  # TODO: adjust to actual id if/when available
]

# Chairman model - synthesizes final response
# Use a model you trust for structured, careful synthesis.
CHAIRMAN_MODEL = "openai/gpt-5.1"
