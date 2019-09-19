'''
@author: Alex Steel
@license: private
@version: v0.0
@attention: Run Command: 
            py.test -v -s -r a --full-trace --color=yes --tb=long --cov
@attention: Generate Coverage
            coverage xml
'''
import base64
challenge_information = [base64.b64decode('aHR0cDovL25ld3RvdXJzLmRlbW9hdXQuY29tLw==')]