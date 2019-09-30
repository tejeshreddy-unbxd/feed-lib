import re

class AttributeNameConversion:
    def __inUnbxdFormat__(self, field_name):
        pattern = re.compile('[a-zA-Z_][a-zA-Z0-9_\\\\-]*(?<!_)$')
        if pattern.match(field_name) is not None:
            return True
        else:
            return False

    def __toUnbxdFormat__(self, field_name):
        key = re.sub('[_-]+$', '', re.sub('^-+', '', re.sub('[^A-Za-z0-9_-]+', '', field_name)))
        firstletter = key[0]
        if firstletter.isdigit():
            key = "_" + re.sub('[_-]+$', "", key)
        else:
            key = re.sub('[_-]+$', "", key)
        return key

    def __conversionAttributeName__(self, field_name):
        pFieldName = field_name
        if pFieldName[0] == '_':
            pFieldName = pFieldName[1:]
        if pFieldName[-1:] == '_':
            pFieldName = pFieldName[-1:]
        pFieldName = re.sub(r'[^\sa-zA-Z0-9\_]', '', pFieldName).strip()
        pFieldName = pFieldName.strip().replace(' ', '_')  
        return pFieldName

    def __run__(self, value):
        if not self.__inUnbxdFormat__(value):
            return self.__toUnbxdFormat__(value)
        else:
            return value
    