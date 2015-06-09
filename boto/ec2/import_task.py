from boto.ec2.ec2object import TaggedEC2Object

class ImportSnapshotTask(TaggedEC2Object):
    """
    Represents an EC2 ImportSnapshotTask
    """

    def __init__(self, connection=None):
        TaggedEC2Object.__init__(self, connection)
        self.request_id = None
        self.description = None
        self.id = None
        self.disk_image_size = None
        self.format = None
        self.snapshot_id = None
        self.progress = None
        self.status = None
        self.status_message = None
        self.url = None
        self.bucket_name = None
        self.bucket_path = None

    def __repr__(self):
        return 'ImportSnapshotTask:%s' % self.id

    def endElement(self, name, value, connection):
        if name == 'description':
            self.description = value
        elif name == 'importTaskId':
            self.id = value
        elif name == 'diskImageSize':
            self.disk_image_size = value
        elif name == 'format':
            self.format = value
        elif name == 'snapshotId':
            self.snapshot_id = value
        elif name == 'progress':
            self.progress = value
        elif name == 'status':
            self.status = value
        elif name == 'statusMessage':
            self.status_message = value
        elif name == 'url':
            self.url = value
        elif name == 's3Bucket':
            self.bucket_name = value
        elif name == 's3Key':
            self.bucket_path = value
        else:
            setattr(self, name, value)


class UserBucketDetails():
    def __init__(self, connection=None):
        TaggedEC2Object.__init__(self, connection)
        self.bucket_name = None
        self.bucket_path = None

    def endElement(self, name, value, connection):
        if name == 's3Bucket':
            self.bucket_name = value
        elif name == 's3Key':
            self.bucket_path = value


class SnapshotDetails(list):

    def startElement(self, name, attrs, connection):
        pass

    def endElement(self, name, value, connection):
        if name == 'snapshotDetail':
            self.append(value)

class ImportImageTask(TaggedEC2Object):
    """
    Represents an EC2 ImportImageTask
    """

    def __init__(self, connection=None):
        TaggedEC2Object.__init__(self, connection)
        self.request_id = None
        self.architecture = None
        self.description = None
        self.hypervisor = None
        self.image_id = None
        self.id = None
        self.license_type = None
        self.platform = None
        self.progress = None
        self.snapshot_details = None
        self.status = None
        self.status_message = None
        self.snapshot_details = SnapshotDetails()

    def __repr__(self):
        return 'ImportImageTask:%s' % self.image_id

    def startElement(self, name, attrs, connection):
        retval = TaggedEC2Object.startElement(self, name, attrs, connection)
        if retval is not None:
            return retval
        elif name == 'snapshotDetails':
            return self.snapshot_details
        else:
            return None
        
    def endElement(self, name, value, connection):
        if name == 'architecture':
            self.architecture = value
        elif name == 'description':
            self.description = value
        elif name == 'hypervisor':
            self.hypervisor = value
        elif name == 'imageId':
            self.image_id = value
        elif name == 'importTaskId':
            self.id = value
        elif name == 'licenseType':
            self.license_type = value
        elif name == 'platform':
            self.platform = value
        elif name == 'progress':
            self.progress = value
        elif name == 'snapshotDetail':
            self.attrs['snapshot_details'].append(value)
        elif name == 'status':
            self.status = value
        elif name == 'statusMessage':
            self.status_message = value