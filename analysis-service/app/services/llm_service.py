import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from app.schemas.analysis import AnalysisResponse
from app.schemas.intelligence import AIAnalysis


load_dotenv()


class LLMService:

    def __init__(self):
        self.client = OpenAI(
            base_url='https://openrouter.ai/api/v1',
            api_key=os.getenv('OPENROUTER_API_KEY')
        )

        self.model = os.getenv(
            'OPENROUTER_MODEL',
            'openrouter/free'
        )

    def analyze(self, analysis: AnalysisResponse) -> AIAnalysis:

        analysis_json = analysis.model_dump_json(indent=2)

        response = self.client.chat.completions.create(
            response_format={
                'type': 'json_schema',
                'json_schema': {
                    'name': 'ai_analysis',
                    'strict': True,
                    'schema': AIAnalysis.model_json_schema()
                }
            },
            
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': (
                        'You are an expert reverse-engineering analyst. '
                        'You are given structured static-analysis evidence '
                        'from a Windows PE executable. '

                        'Analyze the evidence and identify notable behaviors, '
                        'relationships, anomalies, or characteristics. '

                        'Separate direct observations from interpretations. '

                        'Do not claim that a behavior exists unless the provided '
                        'evidence supports it. When evidence is insufficient to '
                        'establish a conclusion, express that uncertainty in the '
                        'interpretation. '

                        'Do not invent addresses, instructions, imports, strings, '
                        'or other evidence. '

                        'For every finding, identify the specific evidence '
                        'supporting it.'
                    )
                },
                {
                    'role': 'user',
                    'content': (
                        'Analyze the following PE analysis results. '
                        'Identify notable behaviors or characteristics '
                        'and explain the evidence supporting them.\n\n'
                        f'{analysis_json}'
                    )
                }
            ]
        )

        print("RAW LLM CONTENT:")
        print(repr(response.choices[0].message.content))

        content = response.choices[0].message.content

        return AIAnalysis.model_validate(
            json.loads(content)
        )
