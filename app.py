from flask import request, jsonify, Flask
from flask_cors import CORS
from utils.db import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
# mysql setting
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/TARA_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False
db.init_app(app)


@app.route('/test', methods=['POST'])
def test():
    data_get = request.json
    print(data_get)
    res = {}
    nodes = []
    edges = []
    node_label2id = {}
    for list in data_get['node']:
        tmp = {}
        node_label2id[list['id']] = list['label']
        tmp['Func_'] = 'fuction_' + list['label']
        tmp['Asset_'] = 'asset_' + list['label']
        tmp['label'] = list['label'] + list['label']
        tmp['S'] = 'X' if str(list['S']) == 'True' else '-'
        tmp['T'] = 'X' if str(list['T']) == 'True' else '-'
        tmp['R'] = 'X' if str(list['R']) == 'True' else '-'
        tmp['I'] = 'X' if str(list['I']) == 'True' else '-'
        tmp['D'] = 'X' if str(list['D']) == 'True' else '-'
        tmp['E'] = 'X' if str(list['E']) == 'True' else '-'
        tmp['Scenario'] = 'Scenario' + list['label']
        nodes.append(tmp)
    for list in data_get['edge']:
        tmp = {}
        tmp['label'] = list['label']
        tmp['Func_'] = 'fuction_' + list['label']
        tmp['Asset_'] = 'asset_' + list['label']
        tmp['S'] = 'X' if str(list['S']) == 'True' else '-'
        tmp['T'] = 'X' if str(list['T']) == 'True' else '-'
        tmp['R'] = 'X' if str(list['R']) == 'True' else '-'
        tmp['I'] = 'X' if str(list['I']) == 'True' else '-'
        tmp['D'] = 'X' if str(list['D']) == 'True' else '-'
        tmp['E'] = 'X' if str(list['E']) == 'True' else '-'
        tmp['Scenario'] = 'Scenario_' + list['label']
        edges.append(tmp)
    threat = [{'Scenario':'Scenario_T-Box','Threat':'Threat_T-Box'},{'Scenario':'Scenario_GW','Threat':'Threat_GW'},{'Scenario':'Scenario_CAN','Threat':'Threat_CAN'}]
    tara = [{'Threat':'Threat_T-Box','Attack_Path': 'Attack_Path_T-Box','Attack_Feasibility':'Attack_Feasibility_T-Box','Impact': 'Impact_T-Box','Risk_Value':'Risk_Value_T-Box','Goal': 'Goal_T-Box'},
            {'Threat':'Threat_GW','Attack_Path': 'Attack_Path_GW','Attack_Feasibility':'Attack_Feasibility_GW','Impact': 'Impact_GW','Risk_Value':'Risk_Value_GW','Goal': 'Goal_GW'},
            {'Threat':'Threat_CAN','Attack_Path': 'Attack_Path_CAN','Attack_Feasibility':'Attack_Feasibility_CAN','Impact': 'Impact_CAN','Risk_Value':'Risk_Value_CAN','Goal': 'Goal_CAN'}]
    countermeasure = [{'Threat':'Threat_T-Box','Asset_':'asset_T-Box','Risk_Value':'Risk_Value_T-Box','CounterMeasure':'CounterMeasure_T-Box'},
        {'Threat': 'Threat_GW', 'Asset_': 'asset_GW', 'Risk_Value': 'Risk_Value_GW','CounterMeasure': 'CounterMeasure_GW'},
        {'Threat': 'Threat_CAN', 'Asset_': 'asset_CAN', 'Risk_Value': 'Risk_Value_CAN','CounterMeasure': 'CounterMeasure_CAN'}]

    print(nodes)
    print(edges)
    print(threat)
    print(tara)
    print(countermeasure)
    res['nodes'] = nodes
    res['edges'] = edges
    res['Scenario_Threat'] = threat
    res['tara'] = tara
    res['countermeasure'] = countermeasure
    # mysql_test = Car.query.filter(Car.cid == 'car_default').first()
    # print(mysql_test.owner)
    # mysql_test.owner += 1
    # db.session.commit()
    return jsonify(res)


if __name__ == '__main__':
    app.run()
