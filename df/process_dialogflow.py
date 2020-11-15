import dialogflow_v2 as dialogflow

'''
response_id: "4de82a92-83e3-4f53-81e8-e6617b12a0a2-ee7586fb"
query_result {
  query_text: "ora-12345"
  parameters {
    fields {
      key: "number"
      value {
        number_value: 12345.0
      }
    }
  }
  all_required_params_present: true
  fulfillment_text: "12345"
  fulfillment_messages {
    text {
      text: "12345"
    }
  }
  intent {
    name: "projects/chatbot-proj-295114/agent/intents/036ffdd6-663a-4230-a2bc-da35ede5e736"
    display_name: "oracle_error"
  }
  intent_detection_confidence: 0.7377335429191589
  language_code: "ko"
}
'''

def detect_intent_texts(project_id, session_id, texts, language_code):
    # session 생성
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    # print('Session path: {}\n'.format(session))

    #for text in texts:
    text_input = dialogflow.types.TextInput(
                text=str(texts), language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
                session=session, query_input=query_input)

    # print('=' * 20)
    # print(response)
    # print('Query text: {}'.format(response.query_result.query_text))
    # print('Detected intent: {} (confidence: {})\n'.format(
    #     response.query_result.intent.display_name,
    #     response.query_result.intent_detection_confidence))
    fulfillment_text = response.query_result.fulfillment_text
    intent = response.query_result.intent.display_name
    # print(response.query_result.parameters.fields['number'])
    # print('Fulfillment text: {}\n'.format(fulfillment_text))
    return intent, fulfillment_text

def create_intent(project_id):
    intent_client = dialogflow.IntentsClient()
    parent = intent_client.project_agent_path(project_id)

    display_name = "create_intent_test"

    # intent = {} #json format
    training_phrases_parts = ['example', 'test']
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    # text response
    message_texts = ['ok', 'thanks']

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intent_client.create_intent(parent, intent)

def update_intent(project_id, intent):
    intent_client = dialogflow.IntentsClient()
    str_training = str(intent.training_phrases)
    print(str_training.find('parts'))
    print(str_training)
    training_pharses_parts = []
    print(list(str_training))
    # json_str = json.loads(str_training)
    # training_phrases_parts.append()
    training_phrases_parts = ['examples', 'tests']
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    intent_id = str("7fb45f6d-da59-423a-b179-b020490574a7")
    name = intent_client.intent_path(project_id, intent_id)
    response = intent_client.get_intent(name)

    response.training_phrases.extend(training_phrases)
    # print(intent)
    # response = intent_client.update_intent(intent)

def delete_intent(project_id, intent_id):
    intents_client = dialogflow.IntentsClient()
    intent_path = intents_client.intent_path(project_id, intent_id)
    intents_client.delete_intent(intent_path)
