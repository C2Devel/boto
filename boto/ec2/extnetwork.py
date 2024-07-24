# Copyright (c) 2017 CROC Incorporated, http://cloud.croc.ru/en/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


from boto.ec2.ec2object import EC2Object


class ExtNetwork(EC2Object):
    """
    Represents an EC2 External Networks.
    """

    def __init__(self, connection = None):
        super(ExtNetwork, self).__init__(connection)
        self.extnet_name = None
        self.state = None
        self.availability_zone = None

    def endElement(self, name, value, connection):
        if name == "extNetId":
            self.extnet_id = value
        elif name == "extNetName":
            self.extnet_name = value
        elif name == "state":
            self.state = value
        elif name == 'availabilityZone':
            self.availability_zone = value
        else:
            setattr(self, name, value)
