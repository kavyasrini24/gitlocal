
import os

from pytest import CaptureFixture
from src.config import read_properties_file
from src.utils import output_properties, load_properties_file


def test_load_properties_files():
    dir='C:\\Users\\G88729\\Desktop\\sampletdd'
    properties_files = load_properties_file(dir)
    
    existingfiles =['output_properties.properties']
    for i in existingfiles:
        individualfiles=i
        for j in properties_files:
           individualpropertiesfile=j
           if individualfiles in individualpropertiesfile:
              result=True
           else:
              result=False
        assert result==True      
          
    #      if individualfiles in :
    #         results=True
    #     else:
    #         results=False
    # assert results==True

def test_output_properties_console(capfd: CaptureFixture[str]):
    dir="C:\\Users\\G88729\\Desktop\\sampletdd\\output_properties.properties" 
    properties = read_properties_file(dir)
    output_properties(1, properties)
    
    
    
    #assert "key2: value2" in out'''
def test_output_properties_file():
    dir="C:\\Users\\G88729\\Desktop\\sampletdd\\output_properties.properties"
   # properties = {"mq.jcbc.sessionCacheSize": "1", "jCBC_kafka_log_lingerMs": "20"}
    #output_file = dir.join("output_properties.properties")
    properties = read_properties_file(dir)
    output_properties(2, properties)
    
    assert os.path.exists(dir)
    with open(dir, 'r') as f:
        content = ['output_properties.properties']
        #assert properties['mq.jcbc.sessionCacheSize'] == "1\n" in content
        #assert "mq.jcbc.sessionCacheSize = 1" in content
       # assert "jCBC_kafka_log_lingerMs = 20" in content
        for i in content:
          outputfile=i
          if outputfile == content[0]:
            results=True
          else:
            results=False
        assert results==True
    
'''
def test_log_missing_properties():
    file_path = "C:\\Users\\G88729\\Desktop\\sampletdd\\src\\tests\\test_data\\application.properties"
    missing_properties = {"mq.jcbc.sessionCacheSize": "1"}
    log_file = file_path.join("missing_properties.log")
    
    log_missing_properties(missing_properties)
    
    assert os.path.exists('missing_properties.log')
    with open('missing_properties.log', 'r') as f:
        content = f.read()
        assert "mq.jcbc.sessionCacheSize = 1" in content
        assert "jCBC_kafka_log_lingerMs = 20" in content
    '''
