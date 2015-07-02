from boto.ec2.ec2object import TaggedEC2Object


class ExportTask(TaggedEC2Object):
    """
    Represents an EC2 ImportTask
    """

    def __init__(self, connection=None):
        TaggedEC2Object.__init__(self, connection)
        self.request_id = None
        self.description = None
        self.id = None
        self.container_format = None
        self.disk_image_format = None
        self.s3_bucket = None
        self.s3_key = None
        self.instance_id = None
        self.target_environment = None
        self.state = None
        self.status_message = None
        
    def endElement(self, name, value, connection):
        if name == 'description':
            self.description = value
        elif name == 'exportTaskId':
            self.id = value
        elif name == 'containerFormat':
            self.container_format= value
        elif name == 'diskImageFormat':
            self.disk_image_format = value
        elif name == 's3Bucket':
            self.s3_bucket = value
        elif name == 's3Key':
            self.s3_key = value
        elif name == 'instanceId':
            self.instance_id = value
        elif name == 'targetEnvironment':
            self.target_environment = value
        elif name == 'state':
            self.state = value
        elif name == 'statusMessage':
            self.status_message= value
