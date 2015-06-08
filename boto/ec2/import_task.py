from boto.ec2.ec2object import TaggedEC2Object


class SnapshotDetails(list):
    def startElement(self, name, attrs, connection):
        pass

    def endElement(self, name, value, connection):
        if name == 'snapshotDetail':
            self.append(value)


class ImportTask(TaggedEC2Object):
    """
    Represents an EC2 ImportTask
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
        self.snapshot_details = SnapshotDetails()
        self.status = None
        self.status_message = None

    def __repr__(self):
        return 'ImportTask:%s' % self.image_id

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
        elif name == 'progress':
            self.progress = value
        elif name == 'status':
            self.status = value
        elif name == 'statusMessage':
            self.status_message = value