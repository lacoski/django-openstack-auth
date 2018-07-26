from abc import ABC, abstractmethod

class Auth_Base(ABC):
    auth_url = ''
    region_site = ''
    domain_id = ''
    domain_name = ''
    project_id = ''
    project_name = ''

    def __init__(self, auth_url = None, region_site = None, domain_id = None, 
                domain_name = None, project_id = None, project_name = None):
        self.auth_url = auth_url
        self.region_site = region_site
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.project_id = project_id
        self.project_name = project_name

    @abstractmethod
    def authenticate_type(self):             
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return self.auth_url + " " + self.region_site + " " + self.domain_id + " " + self.domain_name + \
                     " " + self.project_id + " " + self.project_name

class Auth_Password(Auth_Base):   
    user_name = ''
    user_password = ''

    def __init__(self, auth_url = None, region_site = None, domain_id = None, 
                    domain_name = None, project_id = None, project_name = None, 
                    user_name = None, user_password = None):
        super().__init__(auth_url, region_site, domain_id, domain_name, project_id, project_name)
        self.user_name = user_name
        self.user_password = user_password

    def __str__(self):
        return super().__str__() + " " + self.user_name + " " + self.user_password

    def authenticate_type(self):             
        return 'Password'

class Auth_Token(Auth_Base):   
    token_string = ''

    def __init__(self, auth_url = None, region_site = None, domain_id = None, 
                    domain_name = None, project_id = None, project_name = None, 
                    token_string = None):
        super().__init__(auth_url, region_site, domain_id, domain_name, project_id, project_name)
        self.token_string = token_string

    def __str__(self):
        return super().__str__() + " " + self.token_string
    
    def authenticate_type(self):             
        return 'Token'

def main():
    passwd = Auth_Password(
        auth_url = 'test.com', 
        region_site = 'default', 
        domain_id = 'default', 
        domain_name = 'default', 
        project_id = 'default', 
        project_name = 'default', 
        user_name = 'admin', 
        user_password = '123456'
    )

    token = Auth_Token(
        auth_url = 'test.com', 
        region_site = 'default', 
        domain_id = 'default', 
        domain_name = 'default', 
        project_id = 'default', 
        project_name = 'default', 
        token_string = '123abc12312'
    )
    
    for auth in [passwd, token]:
        print(auth.authenticate_type())


if __name__ == '__main__':
    main()

