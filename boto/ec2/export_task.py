from boto.ec2.ec2object import EC2Object


class ExportTask(EC2Object):
    """
    Represents an EC2 ExportTask
    """

    def __init__(self, connection=None):
        EC2Object.__init__(self, connection)
        self.request_id = None
        self.description = None
        self.id = None
        self.container_format = None
        self.disk_image_format = None
        self.bucket_name = self.s3_bucket = None
        self.bucket_path = self.s3_key = None
        self.instance_id = None
        self.target_environment = None
        self.state = None
        self.status_message = None
        self.volume_export_details = None

    def startElement(self, name, attrs, connection):
        retval = EC2Object.startElement(self, name, attrs, connection)
        if retval is not None:
            return retval

        if name == 'volumeExportDetails':
            self.volume_export_details = VolumeExportDetails()
            return self.volume_export_details
        return None

    def endElement(self, name, value, connection):
        if name == 'exportTaskId':
            self.id = value
        elif name == 'containerFormat':
            self.container_format= value
        elif name == 'diskImageFormat':
            self.disk_image_format = value
        elif name == 's3Bucket':
            self.bucket_name = self.s3_bucket = value
        elif name == 's3Key':
            self.bucket_path = self.s3_key = value
        elif name == 'instanceId':
            self.instance_id = value
        elif name == 'targetEnvironment':
            self.target_environment = value
        elif name == 'statusMessage':
            self.status_message= value
        else:
            setattr(self, name, value)


class ExportVolumeTask(ExportTask):
    """
    Represents custom EC2 ExportVolumeTask
    """

    def __init__(self, connection=None):
        super(ExportVolumeTask, self).__init__(connection)
        self.volume_id = None

    def endElement(self, name, value, connection):
        super(ExportVolumeTask, self).endElement(name, value, connection)
        if name == "volumeId":
            self.volume_id = value


class VolumeExportDetails(list):
    def __init__(self, connection=None):
        list.__init__(self)
        self.connection = connection

    def startElement(self, name, attrs, connection):
        if name == 'item':
            item = ExportVolumeTask(self)
            self.append(item)
            return item

    def endElement(self, name, value, connection):
        pass
