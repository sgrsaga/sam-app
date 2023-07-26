import json
import random
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    
    drink = random_drink()
    message = f"You should drink some {drink}"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "drink": drink
            # "location": ip.text.replace("\n", "")
        }),
    }



def my_func(x):
    return x+5
print("my_func output : " + str(my_func(80)))

func1 = lambda x: x+5
print("func1 output : " + str(func1(20)))

a = [1,4,5,7,6,4,9]
print(a)
newList = list(map(lambda x: x*3, a))
print(newList)


def multiFunc(y):
    return y * 3

print(multiFunc(a))

b = [23,5,2,65,76,7]

def manualFilter(x):
    c = [i for i in x if i>20]
    return c

print(str(manualFilter(b)))

newb = list(filter(lambda x: x>20, b))
print(newb)

def multi(l):
    val = 1
    for i in range(0,len(l)):
        val = val*l[i]
    return val

print(multi(b))

def random_drink():
    drinks = ["coffe","tea","latte","juice"]
    return random.choice(drinks)
