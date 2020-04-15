import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='1b137924-cc7b-41fa-b446-0fc79eac57bf',
  private_key='private.key',
)

ncco = [
  {
    'action': 'talk',
    'voiceName': 'Laila',
    'text': 'Voise'
  }
]

response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': 'here numbber'
  }],
  'from': {
    'type': 'phone',
    'number': '17622131531'
  },
  'ncco': ncco
})

pprint(response)