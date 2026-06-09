import os
import json
import requests
from dotenv import load_dotenv
from app.logger import logger
load_dotenv()

def send_rquest(message): 
    logger.info("Starting whatsapp pipeline.")

    lines = message.split('\n')
    for line in lines:
         if "*ID:*" in line:
             line = line.split('*ID:*')[1].split('-')
             user_id = line[0].replace(' ','')
             question_id = line[1].replace(' ','')
         if "*RESPUESTA:*" in line:
             employee_reply=(line.split('*RESPUESTA:*')[1]).replace(' ','')
    
    
    logger.info("Searching correct url")
    var = os.environ
    url = None

    for i, k in enumerate(var):
        if 'address' in k:
            if str(var.get(k).split('--')[1]) == str(user_id):
                url = var.get(k).split('--')[0]
                logger.info(f"WPP Message belong to user: {user_id}")
                break
            else:
                continue
        else:
            continue

    if url is None:
        logger.info("WPP Message dont belong to this user.")
        return

    msg = {
        'question_id': question_id, 
        'employee_reply':employee_reply
    }

    logger.info("Sending message to Server")
    response = requests.post(url = url, json = json.dumps(msg))
    if response.status_code < 300:
        logger.info("message correctly delivered")
    else:
        logger.error(f"error sending message: {response}")
    return