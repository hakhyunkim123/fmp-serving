# from bson.objectid import ObjectId
# import os, requests
# import sys
# import json
# import dialogflow_v2 as dialogflow
#
# def detect_intent_texts(project_id, session_id, texts, language_code):
#     session_client = dialogflow.SessionsClient()
#
#     session = session_client.session_path(project_id, session_id)
#
#     # for text in texts:
#     text_input = dialogflow.types.TextInput(
#         text=str(texts), language_code=language_code)
#
#     query_input = dialogflow.types.QueryInput(text=text_input)
#
#     response = session_client.detect_intent(
#         session=session, query_input=query_input)
#
#     # print('Query text: {}'.format(response.query_result.query_text))
#     # print('Detected intent: {} (confidence: {})\n'.format(
#     #     response.query_result.intent.display_name,
#     #     response.query_result.intent_detection_confidence))
#     fulfillment_text = response.query_result.fulfillment_text.encode('utf-8')
#     entities = response.query_result.parameters.fields
#     intent = response.query_result.query_text
#     # print('Fulfillment text: {}\n'.format(
#     #     fulfillment_text))
#     return fulfillment_text
#
# def get_intent_info(project_id, session_id):
#     intent_client = dialogflow.IntentsClient()
#     intent_id = str("7fb45f6d-da59-423a-b179-b020490574a7")
#     name = intent_client.intent_path(project_id, intent_id)
#     # print(name)
#     response = intent_client.get_intent(name, intent_view="INTENT_VIEW_FULL")
#     # print(response)
#     update_intent(project_id, response)
#
# def list_intent_info(project_id):
#     intent_client = dialogflow.IntentsClient()
#     parent = intent_client.project_agent_path(project_id)
#     intents = intent_client.list_intents(parent, intent_view="INTENT_VIEW_FULL")
#     for intent in intents:
#         print(intent)
#         print('=' * 20)
#         print('Intent name: {}'.format(intent.name))
#         print('Intent display_name: {}'.format(intent.display_name))
#         print('Action: {}\n'.format(intent.action))
#         print('Root followup intent: {}'.format(
#             intent.root_followup_intent_name))
#         print('Parent followup intent: {}\n'.format(
#             intent.parent_followup_intent_name))
#
#         print('Input contexts:')
#         for input_context_name in intent.input_context_names:
#             print('\tName: {}'.format(input_context_name))
#
#         print('Output contexts:')
#         for output_context in intent.output_contexts:
#             print('\tName: {}'.format(output_context.name))
#
#
# def create_intent(project_id):
#     intent_client = dialogflow.IntentsClient()
#     parent = intent_client.project_agent_path(project_id)
#
#     display_name = "create_intent_test"
#
#     # intent = {} #json format
#     training_phrases_parts = ['example', 'test']
#     training_phrases = []
#     for training_phrases_part in training_phrases_parts:
#         part = dialogflow.types.Intent.TrainingPhrase.Part(
#             text=training_phrases_part)
#         # Here we create a new training phrase for each provided part.
#         training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
#         training_phrases.append(training_phrase)
#     # text response
#     message_texts = ['ok', 'thanks']
#
#     text = dialogflow.types.Intent.Message.Text(text=message_texts)
#     message = dialogflow.types.Intent.Message(text=text)
#
#     intent = dialogflow.types.Intent(
#         display_name=display_name,
#         training_phrases=training_phrases,
#         messages=[message])
#
#     response = intent_client.create_intent(parent, intent)
#
# def update_intent(project_id, intent):
#     intent_client = dialogflow.IntentsClient()
#     str_training = str(intent.training_phrases)
#     print(str_training.find('parts'))
#     print(str_training)
#     training_pharses_parts = []
#     print(list(str_training))
#     # json_str = json.loads(str_training)
#     # training_phrases_parts.append()
#     training_phrases_parts = ['examples', 'tests']
#     training_phrases = []
#     for training_phrases_part in training_phrases_parts:
#         part = dialogflow.types.Intent.TrainingPhrase.Part(
#             text=training_phrases_part)
#         # Here we create a new training phrase for each provided part.
#         training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
#         training_phrases.append(training_phrase)
#
#     intent_id = str("7fb45f6d-da59-423a-b179-b020490574a7")
#     name = intent_client.intent_path(project_id, intent_id)
#     response = intent_client.get_intent(name)
#
#     response.training_phrases.extend(training_phrases)
#     # print(intent)
#     # response = intent_client.update_intent(intent)
#
# def delete_intent(project_id, intent_id):
#     intents_client = dialogflow.IntentsClient()
#     intent_path = intents_client.intent_path(project_id, intent_id)
#     intents_client.delete_intent(intent_path)