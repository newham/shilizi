import json

from django.http import HttpResponse
from .model import neural_network as nn
from .model import dataset

input_nodes = 28 * 28
hidden_nodes = 100
output_nodes = 10
learning_rate = 0.2
neural_network = nn.NeuralNetwork(input_nodes, hidden_nodes,
                                  output_nodes, learning_rate)
neural_network.load('w_input_hidden.txt', 'w_hidden_output.txt')


def test(request):
    resp = {'code': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def query(request, name=''):
    img_dir = 'static/img/mnist/'
    img_data = dataset.load_img(img_dir + name)
    result = neural_network.query(img_data)
    resp = {'code': 0, 'label': int(result)}
    return HttpResponse(json.dumps(resp), content_type="application/json")
