#EC2 Commandline
easy way to deploy a ec2 instance with the same settings.

##Functionality

```
usage: ec2.py [-h] [-l] [-a instance_type] [-t resource_id desired_name]


ec2 helper

optional arguments:
  -h, --help            show this help message and exit
  -l, --list
  -a instance_type, --add instance_type
                        specify instance_type
  -t resource_id desired_name, --tag resource_id desired_name
                        add instance name: {resource_id} {name}
```

 * --list shows current instance you have
 * --add add a instance_type with t1.micro, m1.small, etc
 * --tag add a name to the instance you just created using the resource_id it returned, right now doesn't support existing instances
 
##Installation

```
virtualenv ev #setup virtual environment
source ev/bin/activate #activate virtual environment
pip install -r requirements.txt #install dependency
```

##Config File
```
config.py #for default configurations
credentials.py #for ec2 credentials
```


##Run
```
python ec2.py --help
```

##License
```
The MIT License (MIT)

Copyright (c) 2013 Jianer Shi (hipaulshi@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
