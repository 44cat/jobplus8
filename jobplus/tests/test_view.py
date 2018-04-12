from flask import url_for

class TestIndex:
    
    endpoint = 'front.index'

    def test_index(self,client):
        response = client.get(url_for(self.endpoint))

        assert response.status_code == 200

class TestCompany:

    endpoint = 'company.index'

    def test_index(self,client):
        response = client.get(url_for(self.endpoint))

        assert response.status_code == 200

class TestJob:
    endpoint = 'job.index'

    def test_index(self,client):
        response = client.get(url_for.endpoint))

        assert response.status_code == 200

class TestAdmin:
    endpoint = 'admin.index'

    def test_index(self,client):
        response = client.get(url_for(self.endpoint))

        assert response.status_code == 403
