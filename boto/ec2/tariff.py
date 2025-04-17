"""Croc Cloud EC2 Tariff."""

from boto.resultset import ResultSet
from decimal import Decimal

class Tariff(object):
    def __init__(self, connection=None):
        self.name = None
        self.currency = None
        self.description = None
        self.instances = None
        self.instance_types = None
        self.volumes = None
        self.others = None
        self.oses = None
        self.hosts = None

    def startElement(self, name, attrs, connection):
        if name == 'instances':
            self.instances = ResultSet([('item', TariffInstance)])
            return self.instances
        elif name == 'volumes':
            self.volumes = ResultSet([('item', TariffVolume)])
            return self.volumes
        elif name == 'others':
            self.others = ResultSet([('item', TariffService)])
            return self.others
        elif name == 'oses':
            self.oses = ResultSet([('item', TariffOS)])
            return self.oses
        elif name == 'instance_types':
            self.instance_types = ResultSet([('item', TariffInstanceType)])
            return self.instance_types
        elif name == 'hosts':
            self.hosts = ResultSet([('item', TariffHostType)])
            return self.hosts
        else:
            return None

    def endElement(self, name, value, connection):
        if name == 'name':
            self.name = value
        elif name == 'currency':
            self.currency = value
        elif name == 'description':
            self.description = value
        else:
            setattr(self, name, value)


class TariffInstance(object):
    def __init__(self, connection=None):
        self.name = None
        self.cpu = None
        self.ccus = None
        self.memory = None
        self.services = None

    def startElement(self, name, attrs, connection):
        if name == 'services':
            self.services = ResultSet([('item', TariffService)])
            return self.services
        else:
            return None

    def endElement(self, name, value, connection):
        if name == 'name':
            self.name = value
        elif name == 'cpu':
            self.cpu = int(value)
        elif name == 'ccus':
            self.ccus = Decimal(value)
        elif name == 'memory':
            self.memory = int(value)
        else:
            setattr(self, name, value)


class TariffService(object):
    def __init__(self, connection=None):
        self.name = None
        self.description = None
        self.measure = None
        self.rates = None
        self.deprecated = False

    def startElement(self, name, attrs, connection):
        if name == 'rates':
            self.rates = ResultSet([('item', TariffRate)])
            return self.rates
        else:
            return None

    def endElement(self, name, value, connection):
        if name == 'name':
            self.name = value
        elif name == 'description':
            self.description = value
        elif name == 'measure':
            self.measure = value
        elif name == "deprecated":
            self.deprecated = bool(value)
        else:
            setattr(self, name, value)


class TariffRate(object):
    def __init__(self, connection=None):
        self.price = None
        self.availability_zone = None

    def startElement(self, name, attrs, connection):
        return None

    def endElement(self, name, value, connection):
        if name == 'price':
            self.price = Decimal(value)
        elif name == 'availability_zone':
            self.availability_zone = value
        else:
            setattr(self, name, value)


class TariffVolume(TariffService):
    def __init__(self, connection=None):
        super(TariffVolume, self).__init__(connection)
        self.type = None
        self.iops = None

    def startElement(self, name, attrs, connection):
        return super(TariffVolume, self).startElement(name, attrs, connection)

    def endElement(self, name, value, connection):
        if name == 'type':
            self.type = value
        elif name == 'iops':
            self.iops = int(value)
        else:
            super(TariffVolume, self).endElement(name, value, connection)


class TariffInstanceType(TariffService):
    def __init__(self, connection=None):
        super(TariffInstanceType, self).__init__(connection)
        self.cpu = None
        self.memory = None
        self.ccus = None

    def endElement(self, name, value, connection):
        if name == 'cpu':
            self.cpu = int(value)
        elif name == 'memory':
            self.memory = int(value)
        elif name == 'ccus':
            self.ccus = Decimal(value)
        else:
            super(TariffInstanceType, self).endElement(name, value, connection)


class TariffLicenceType(object):
    def __init__(self, connection=None):
        self.base = None

    def startElement(self, name, attrs, connection):
        return None

    def endElement(self, name, value, connection):
        if name == 'base':
            self.base = value
        else:
            setattr(self, name, value)


class TariffOS(TariffService):
    def __init__(self, connection=None):
        super(TariffOS, self).__init__(connection)
        self.licence_type = None

    def startElement(self, name, attrs, connection):
        if name == 'licence_type':
            self.licence_type = TariffLicenceType()
            return self.licence_type
        else:
            return super(TariffOS, self).startElement(name, attrs, connection)


class TariffHostType(TariffService):
    def __init__(self, connection=None):
        super(TariffHostType, self).__init__(connection)
        self.cpu_generation = None
        self.physical_cores = None
        self.sockets = None
        self.memory = None
        self.ccus = None
        self.commitment = None
        self.type = None

    def startElement(self, name, attrs, connection):
        return super(TariffHostType, self).startElement(name, attrs, connection)

    def endElement(self, name, value, connection):
        if name == 'cpu_generation':
            self.cpu_generation = value
        elif name == 'physical_cores':
            self.physical_cores = int(value)
        elif name == 'sockets':
            self.sockets = int(value)
        elif name == 'memory':
            self.memory = int(value)
        elif name == 'ccus':
            self.ccus = Decimal(value)
        elif name == 'commitment':
            self.commitment = int(value)
        elif name == 'type':
            self.type = value
        else:
            super(TariffHostType, self).endElement(name, value, connection)
