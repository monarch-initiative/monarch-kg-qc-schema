from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class Report(ConfiguredBaseModel):
    """
    Represents a Report
    """
    dangling_edges: Optional[EdgeReport] = Field(None, description="""Report summarizing knowledge graph dangling edges""")
    edges: EdgeReport = Field(..., description="""Report summarizing knowledge graph edges""")
    nodes: NodeReport = Field(..., description="""Report summarizing knowledge graph nodes""")
    missing_nodes: Optional[NodeReport] = Field(None, description="""Report summarizing knowledge graph missing nodes""")
    


class SubReport(ConfiguredBaseModel):
    """
    An abstract report section for a knowledge graph
    """
    categories: Optional[List[str]] = Field(default_factory=list, description="""The categories of the node or edge objects""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    namespaces: Optional[List[str]] = Field(default_factory=list, description="""The namespaces of the node or edge objects""")
    total_number: Optional[int] = Field(None, description="""Total number of edge or node objects""")
    


class EdgeReport(SubReport):
    """
    A sub report summarizing a collection of edges
    """
    missing: Optional[int] = Field(None, description="""Number of missing of type in collection""")
    node_types: Optional[List[NodeTypeReport]] = Field(default_factory=list, description="""NodeType reports for the edges collection""")
    predicates: Optional[List[PredicateReport]] = Field(default_factory=list, description="""Predicate reports for the edges collection""")
    categories: Optional[List[str]] = Field(default_factory=list, description="""The categories of the node or edge objects""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    namespaces: Optional[List[str]] = Field(default_factory=list, description="""The namespaces of the node or edge objects""")
    total_number: Optional[int] = Field(None, description="""Total number of edge or node objects""")
    


class NodeReport(SubReport):
    """
    A sub report summarizing a collection of nodes
    """
    taxon: Optional[List[str]] = Field(default_factory=list, description="""The taxons of the nodes in the collection""")
    categories: Optional[List[str]] = Field(default_factory=list, description="""The categories of the node or edge objects""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    namespaces: Optional[List[str]] = Field(default_factory=list, description="""The namespaces of the node or edge objects""")
    total_number: Optional[int] = Field(None, description="""Total number of edge or node objects""")
    


class NodeTypeReport(NodeReport):
    """
    A sub report summarizing the types of a collection of nodes
    """
    missing: Optional[int] = Field(None, description="""Number of missing of type in collection""")
    taxon: Optional[List[str]] = Field(default_factory=list, description="""The taxons of the nodes in the collection""")
    categories: Optional[List[str]] = Field(default_factory=list, description="""The categories of the node or edge objects""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    namespaces: Optional[List[str]] = Field(default_factory=list, description="""The namespaces of the node or edge objects""")
    total_number: Optional[int] = Field(None, description="""Total number of edge or node objects""")
    


class PredicateReport(ConfiguredBaseModel):
    """
    A sub report summarizing the predicates of a collection
    """
    missing_object_namespaces: Optional[List[str]] = Field(default_factory=list, description="""Namespaces of missing objects from predicate edges collection""")
    missing_objects: Optional[int] = Field(None, description="""Number of missing objects in edges of predicate collection""")
    missing_subject_namespaces: Optional[List[str]] = Field(default_factory=list, description="""Namespaces of mission subjects from predicate edges collection""")
    missing_subjects: Optional[int] = Field(None, description="""Number of mission subjects in edges of predicate collection""")
    total_number: Optional[int] = Field(None, description="""Total number of edge or node objects""")
    uri: Optional[str] = Field(None, description="""Predicate URI for the group of edges""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Report.update_forward_refs()
SubReport.update_forward_refs()
EdgeReport.update_forward_refs()
NodeReport.update_forward_refs()
NodeTypeReport.update_forward_refs()
PredicateReport.update_forward_refs()

