from keystoneauth1.identity import v3
from keystoneclient.v3 import client
from keystoneauth1 import session
import openstack
from openstack import connection
from auth_class import (
    Auth_Password,
    Auth_Token,
    Token
)

openstack.enable_logging(debug=True)


def main():
    passwd_auth = Auth_Password(
        auth_url = 'http://172.16.4.200:5000/v3/', 
        region_site = 'RegionOne',         
        project_domain_name = 'default', 
        project_id = '91e4db1098934a3e9cc7babf97edf007', 
        project_name = 'admin',
        user_name = 'admin', 
        user_password = 'Welcome123',
        user_domain_name = 'default'
    )   
    token_auth = Auth_Token(
        auth_url = 'http://172.16.4.200:5000/v3/', 
        region_site = 'RegionOne',         
        project_domain_name = 'default',
        project_id = '91e4db1098934a3e9cc7babf97edf007', 
        project_name = 'admin',
        token_string = 'gAAAAABbWXoknzRlwxMLrmzLcrCb15XhTd3_dAAEL6rgBwsCR7NMQAbKsKWgFH7uT4OZ6jAltTN6zj_LAp-PAD0Zdij0lk4SqI2oj8yWW0ltuKoUIJDDGrBf6gfEiQareA3Fp5OZQdzVqUeyDyNf6ByhGi1pX-dcPYzxzVgiocqmuyEdVL-8CXI'
    )
    token_generate = Token(auth_ref = passwd_auth)
    #print(token_generate.get_token())
    data = token_generate.get_identity()
    print(data.user_domain_id)

    
    # token_generate = Token(auth_ref = token_auth)
    # print(token_generate.is_authenticated())

if __name__ == '__main__':
    main()
