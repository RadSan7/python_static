class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")

    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = []
        for attribute in self.props:
            attributes.append(f' {attribute}="{self.props[attribute]}"')
        return "".join(attributes)
    

class LeafNode(HTMLnode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)





    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have a children")
        
        result = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            if child.children:
                result += child.to_html()
            else: result += (f"<{child.tag}{child.props_to_html()}>{child.value}</{child.tag}>")
        result += f"</{self.tag}>"

        print(result)
        return result