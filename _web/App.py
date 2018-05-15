from flask import Flask, request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from datetime import datetime
# import mRun as mr
# import utils_data as md

app = Flask(__name__)
def app_config():
    pass
    # not working!!!! 
    app.config['SERVER_NAME'] = '127.0.0.1' + ':' + '5001'
    # flask_app.config['SERVER_NAME'] = server_name + ':' + server_port
    # flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION # 'list'
    # flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE # True
    # flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER # False
    # flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP # False 
    #                   - If a request does not match any of the application endpoints => return error 404 or not 

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='FP API',   description='Prototype REST API', )
ns = api.namespace('fp', description='Operations')

#model _______________________________
fp = api.model('fp', {
    # for ABAP I need to set the ids in upper case
    #'id': fields.Integer(readOnly=True, description='The fp unique identifier'),
    'forml': fields.String(required=True, description='form details'),
    'pred' : fields.String(required= False,description='Prediction') })

def get_models(type):
    if type == "MOD1":
        return [
            { 'dt':'C2',  "e":100, "lr":0.001, "h":[100 , 100], "spn": 5000, "pe": [], "pt": [], "ninp":1814  },
            { 'dt':'C4',  "e":100, "lr":0.001, "h":[100 , 100], "spn": 5000, "pe": [], "pt": [], "ninp":1814  },
            { 'dt':'C1',  "e":100, "lr":0.001, "h":[100 , 100], "spn": 5000, "pe": [], "pt": [], "ninp":1814  },
        ]
    elif type == "MOD2":
        return [
            { 'dt':'C2',  "e":40,  "lr":0.001, "h":[100 , 100], "spn": 10000, "pe": [], "pt": [], "ninp":2385  },
            { 'dt':'C4',  "e":100, "lr":0.001, "h":[100 , 100], "spn": 10000, "pe": [], "pt": [], "ninp":2385  },
            { 'dt':'C1',  "e":100, "lr":0.001, "h":[100 , 100], "spn": 10000, "pe": [], "pt": [], "ninp":2385  },
        ]
    else: return []

class fpDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, forml , ret_str = True ):
        print("___Start!___" +  datetime.now().strftime('%H:%M:%S')  )
        # md.setDESC(md.DESC) 
        # execc = get_models(md.DESC);   
        # ex = execc[2]; md.spn = ex["spn"]; md.dType = ex["dt"]; mr.epochs = ex["e"]; mr.lr = ex["lr"]; mr.h = ex["h"]; mr.ninp = ex["ninp"]
        # mr.ninp, mr.nout, mr.top_k = md.getnn(mr.ninp)
        
        # md.MODEL_DIR = md.LOGDIR + md.DESC + '/'   + mr.get_hpar(mr.epochs, final=final) +"/" 
        # mr.model_path = md.MODEL_DIR + "model.ckpt" 
        # mr.build_network3()                                                                                                                                                                                                                                                                                    
       
        # print(mr.model_path)    
        # ret = mr.tests_exec(forml, ret_str )  
        # if ret_str: rett.append(ret)
        # else:       rett.update(ret)

        return {"pred": 25}
        # for todo in self.todos:
        #     if todo['id'] == id:
        #         return todo
        # api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):        return "create"
    def update(self, id, data):    return "update"
    def delete(self, id):          return "delete"
DAO = fpDAO()

# _______________________
# ROUTES
# _______________________
@ns.route('/') # POST! 
class fpPredList(Resource):
    @ns.doc('get dummy')
    @ns.marshal_list_with(fp)
    def get(self):
        return {   "pred": "25",  "forml": "GET" }

    @ns.doc('post form and get fp')
    @ns.expect(fp)
    @ns.marshal_with(fp, code=201)
    def post(self):
        forml2 = api.payload["forml"]
        forml2 = forml2.replace("'", '"'); print(forml2)
        
        ret_st  = api.payload["RET_STR"]
        ret_str = ( True  if ( ret_st == "X" ) else  False )
        # ret_str = "X"#False
        ret_str = False
        
        pred = DAO.get(forml2)
        pred = DAO.get(forml2, ret_str)
        
        api.payload["FORML"] = "Done"

        # 1 
        # api.payload["pred"] = pred
        
        #2
        if ret_str: 
            api.payload["PRED"] = pred
            api.payload["PRED_C2_0"] = pred[0]
            api.payload["PRED_C4_0"] = pred[1]
            api.payload["PRED_C1_0"] = pred[2]
        else: 
            api.payload["PRED"] = "SEPARATION! ret_str = False!"
            api.payload.update(pred)
        
        return api.payload
        # return DAO.create(api.payload), 201
        # EXAMPLE
        ex = {
               "forml": "{ 'm':'1', '10' : 1 }",
               "pred": "string"
             }

@api.route('/<string:forml>')
# api.add_resource(Todo, '/todo/<int:todo_id>', endpoint='todo_ep')
# @api.route('/todo/<int:todo_id>', endpoint='todo_ep')
@ns.param('forml', 'Dummy par - not working!')
class fpPred(Resource):
    def get(self, forml):
        pred = 201
        if (len(request.form) > 0):
            forml2 = request.form['data'];  print(forml2)
            pred = DAO.get(forml2)
        # print(forml) # this is not working! 
        print(pred)
        return {"pred": pred}

    def put(self, forml):
        # forml = request.form['data']
        print(forml)
        return {"pred": 25}


# _______________________
# TESTS
# _______________________
def test_curl():
    pass
    # json_str = '''[
    #     { "m":"2", "tomato" :0.74598 , "pasta" :0.1 , "salt" :0.04  }   
    #     { "m":"1", "c10" : 1 }
    #     tmpLab = [50, 73]
    # $ curl http://localhost:5000/FORML{213} -d "data=Change my brakepads" -X GET
    # curl http://localhost:5000/form1Level -d "data='{ "m":"2", "tomato" :0.74598 , "salt" :0.1  }'" -X GET
    # curl http://localhost:5000/123 -d "data='{"m":"1","c10":1}'" -X GET
    #.curl http://localhost:5000/todo1    
    # API.payload
    # {
    #   "hello": "{ 'm':'1', 'c10' : 1 }",
    #   "pred": "string"
    # }

def single_tests():
    """triple comment = treated as string """
    real = 50; #pred 68 , 67 -around 15%
    forml2 = '''{ "m":"01", "tomate" :0.74598 , 
                            "pasta" :0.1 , 
                            "salt" :0.04 ,  
                            "pepper" :0.0001 }  ''' 
    # real = 73 #pred 73 high, 77,74...
    # forml2 = '''{ "m":"1", "10" : 1 } '''
    real = 54 #pred 57, 58 low prod
    forml2 = '''{ "m":"02",     "pasta" :0.31245 , 
                                "rice" :0.1 , 
                                "salt" :0.001 , 
                                "pepper" :0.001 , 
                                "chicken" :0.001 , 
                                "cucumber" :0.0005 , 
                                "pinaple" :0.0005 , 
                                "tomato" :0.0005 , 
                                "c10" :0.0005 , 
                                "c20" :0.00005 } '''; 
    # real = 101 #pred 101, 100
    # forml2 = '''{ "m":"03",     "c10" :1 } '''
    # beginc = """
    real = 88  #pred 89,88
    forml2 = '''{ "m":"03",     "pasta" :0.531 , 
                                "tomato" :0.2 ,   
                                "salt" :0.005 , 
                                "pepper" :0.004 }   '''
    beginc = """
    """ #end of comment
    
    pred = DAO.get(forml2)
    print("\n\n\n_R = {} and P = {}" .format(real ,pred ) )

    # print(md.dsp[["M","FP"]]);     # print(md.dsp.iloc[0])
    # md.print_form2(md.dsp.iloc[0])

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)  # accessible from the network! 
    # single_tests()   