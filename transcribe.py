from deepgram import Deepgram
import asyncio, json
import os
from dotenv import load_dotenv

load_dotenv()


DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

FILE = "bueller-life-moves-pretty-fast_uud9ip.wav"

MIMETYPE = "wav"

async def main():
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    
    if FILE.startswith('http'):
        source = {
            'url': FILE
        }
    else:
        audio = open(FILE, 'rb')
        
        source = {
            'buffer':audio,
            'mimetype': MIMETYPE
        }
    
    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                'smart_format':True,
                'model': 'nova-2',
            }
        )
    )
    
    print(json.dumps(response, indent=4))
    
try:
  # If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
  #await main()
  asyncio.run(main())
except Exception as e:
  exception_type, exception_object, exception_traceback = sys.exc_info()
  line_number = exception_traceback.tb_lineno
  print(f'line {line_number}: {exception_type} - {e}')