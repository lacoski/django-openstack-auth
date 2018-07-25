from keystoneauth1.identity import v3
from keystoneclient.v3 import client
from keystoneauth1 import session
import openstack
from openstack import connection

openstack.enable_logging(debug=True)


def main():
    # auth = v3.Password(
    #     auth_url='http://172.16.4.200:5000/v3/',
    #     user_id='659edb24617f4ca785f35dcb9d926f2b',
    #     password='Welcome123',
    #     project_id='91e4db1098934a3e9cc7babf97edf007',
    #     project_domain_name='default',
    #     user_domain_name='default'
    # )
    auth = v3.Token(
        auth_url='http://172.16.4.200:5000/v3/',
        token='gAAAAABbV_vrVeaP6__4K97qA6qK5px13iQ4JAu7T4BO79vDOth0nkC-EHpuE_DNcfvgFTO_LtaELX7vpvvCJ8QmUAFdqmu865KFowADBKfhfzFjeMw_Bs-Yps5jTReI1XuP2E2jbyFfSrl8c8Dktb8p-H6G8bSJmy_xGyNbv6cdZ03qs6yT98s',
        project_id='91e4db1098934a3e9cc7babf97edf007',
        project_domain_name='default',
        # user_domain_name='default'
    )

    sess = session.Session(auth=auth)
    
    # sess.get('http://172.16.4.200:5000/v3/',
    #                 authenticated=True)
    # keystone = client.Client(session=sess)
    # users = keystone.users.list()
    # print(users)

    # resp = sess.get('http://172.16.4.200:5000/v3/', authenticated=True)
    print(sess.get_auth_headers())
    print(sess.get_auth_headers())
    ###
    conn = connection.Connection(        
        session = sess,
        identity_api_version='3',
        region_name='RegionOne',
        compute_api_version='2',
        identity_interface='internal',
        user_domain_name='default',
        project_domain_name='default'
    )
    for image in conn.compute.servers():
        print(image)


if __name__ == '__main__':
    main()
