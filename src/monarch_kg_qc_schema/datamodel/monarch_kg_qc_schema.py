# Auto generated from monarch_kg_qc_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-25T10:56:44
# Schema: monarch-kg-qc-schema
#
# id: https://w3id.org/monarch-initiative/monarch-kg-qc-schema
# description: Schema for QC reports on the Monarch KG.
# license: BSD-3

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONARCH_KG_QC_SCHEMA = CurieNamespace('monarch_kg_qc_schema', 'https://w3id.org/monarch-initiative/monarch-kg-qc-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MONARCH_KG_QC_SCHEMA


# Types

# Class references



@dataclass
class Report(YAMLRoot):
    """
    Represents a Report
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.Report
    class_class_curie: ClassVar[str] = "monarch_kg_qc_schema:Report"
    class_name: ClassVar[str] = "Report"
    class_model_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.Report

    dangling_edges: Optional[Union[Union[dict, "EdgeReport"], List[Union[dict, "EdgeReport"]]]] = empty_list()
    edges: Optional[Union[Union[dict, "EdgeReport"], List[Union[dict, "EdgeReport"]]]] = empty_list()
    nodes: Optional[Union[Union[dict, "NodeReport"], List[Union[dict, "NodeReport"]]]] = empty_list()
    missing_nodes: Optional[Union[Union[dict, "NodeReport"], List[Union[dict, "NodeReport"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.dangling_edges, list):
            self.dangling_edges = [self.dangling_edges] if self.dangling_edges is not None else []
        self.dangling_edges = [v if isinstance(v, EdgeReport) else EdgeReport(**as_dict(v)) for v in self.dangling_edges]

        if not isinstance(self.edges, list):
            self.edges = [self.edges] if self.edges is not None else []
        self.edges = [v if isinstance(v, EdgeReport) else EdgeReport(**as_dict(v)) for v in self.edges]

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, NodeReport) else NodeReport(**as_dict(v)) for v in self.nodes]

        if not isinstance(self.missing_nodes, list):
            self.missing_nodes = [self.missing_nodes] if self.missing_nodes is not None else []
        self.missing_nodes = [v if isinstance(v, NodeReport) else NodeReport(**as_dict(v)) for v in self.missing_nodes]

        super().__post_init__(**kwargs)


@dataclass
class SubReport(YAMLRoot):
    """
    Represents a report section for a knowledge graph of entity type
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.SubReport
    class_class_curie: ClassVar[str] = "monarch_kg_qc_schema:SubReport"
    class_name: ClassVar[str] = "SubReport"
    class_model_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.SubReport

    categories: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    name: Optional[str] = None
    namespaces: Optional[Union[str, List[str]]] = empty_list()
    total_number: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.namespaces, list):
            self.namespaces = [self.namespaces] if self.namespaces is not None else []
        self.namespaces = [v if isinstance(v, str) else str(v) for v in self.namespaces]

        if self.total_number is not None and not isinstance(self.total_number, int):
            self.total_number = int(self.total_number)

        super().__post_init__(**kwargs)


@dataclass
class EdgeReport(SubReport):
    """
    Represents a sub report for a collection of edges
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.EdgeReport
    class_class_curie: ClassVar[str] = "monarch_kg_qc_schema:EdgeReport"
    class_name: ClassVar[str] = "EdgeReport"
    class_model_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.EdgeReport

    missing: Optional[int] = None
    node_types: Optional[Union[Union[dict, "NodeTypeReport"], List[Union[dict, "NodeTypeReport"]]]] = empty_list()
    predicates: Optional[Union[Union[dict, "PredicateReport"], List[Union[dict, "PredicateReport"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.missing is not None and not isinstance(self.missing, int):
            self.missing = int(self.missing)

        if not isinstance(self.node_types, list):
            self.node_types = [self.node_types] if self.node_types is not None else []
        self.node_types = [v if isinstance(v, NodeTypeReport) else NodeTypeReport(**as_dict(v)) for v in self.node_types]

        if not isinstance(self.predicates, list):
            self.predicates = [self.predicates] if self.predicates is not None else []
        self.predicates = [v if isinstance(v, PredicateReport) else PredicateReport(**as_dict(v)) for v in self.predicates]

        super().__post_init__(**kwargs)


@dataclass
class NodeReport(SubReport):
    """
    Represents a sub report for a collection of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.NodeReport
    class_class_curie: ClassVar[str] = "monarch_kg_qc_schema:NodeReport"
    class_name: ClassVar[str] = "NodeReport"
    class_model_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.NodeReport

    taxon: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.taxon, list):
            self.taxon = [self.taxon] if self.taxon is not None else []
        self.taxon = [v if isinstance(v, str) else str(v) for v in self.taxon]

        super().__post_init__(**kwargs)


@dataclass
class NodeTypeReport(NodeReport):
    """
    Represents a report for a collection of nodes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.NodeTypeReport
    class_class_curie: ClassVar[str] = "monarch_kg_qc_schema:NodeTypeReport"
    class_name: ClassVar[str] = "NodeTypeReport"
    class_model_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.NodeTypeReport

    missing: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.missing is not None and not isinstance(self.missing, int):
            self.missing = int(self.missing)

        super().__post_init__(**kwargs)


@dataclass
class PredicateReport(YAMLRoot):
    """
    Represents a report for predicates of a collection of edges
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.PredicateReport
    class_class_curie: ClassVar[str] = "monarch_kg_qc_schema:PredicateReport"
    class_name: ClassVar[str] = "PredicateReport"
    class_model_uri: ClassVar[URIRef] = MONARCH_KG_QC_SCHEMA.PredicateReport

    missing_object_namespaces: Optional[Union[str, List[str]]] = empty_list()
    missing_objects: Optional[int] = None
    missing_subject_namespaces: Optional[Union[str, List[str]]] = empty_list()
    missing_subjects: Optional[int] = None
    total_number: Optional[int] = None
    uri: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.missing_object_namespaces, list):
            self.missing_object_namespaces = [self.missing_object_namespaces] if self.missing_object_namespaces is not None else []
        self.missing_object_namespaces = [v if isinstance(v, str) else str(v) for v in self.missing_object_namespaces]

        if self.missing_objects is not None and not isinstance(self.missing_objects, int):
            self.missing_objects = int(self.missing_objects)

        if not isinstance(self.missing_subject_namespaces, list):
            self.missing_subject_namespaces = [self.missing_subject_namespaces] if self.missing_subject_namespaces is not None else []
        self.missing_subject_namespaces = [v if isinstance(v, str) else str(v) for v in self.missing_subject_namespaces]

        if self.missing_subjects is not None and not isinstance(self.missing_subjects, int):
            self.missing_subjects = int(self.missing_subjects)

        if self.total_number is not None and not isinstance(self.total_number, int):
            self.total_number = int(self.total_number)

        if self.uri is not None and not isinstance(self.uri, str):
            self.uri = str(self.uri)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.categories = Slot(uri=SCHEMA.categories, name="categories", curie=SCHEMA.curie('categories'),
                   model_uri=MONARCH_KG_QC_SCHEMA.categories, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\S+:\S+'))

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MONARCH_KG_QC_SCHEMA.description, domain=None, range=Optional[str])

slots.missing = Slot(uri=MONARCH_KG_QC_SCHEMA.missing, name="missing", curie=MONARCH_KG_QC_SCHEMA.curie('missing'),
                   model_uri=MONARCH_KG_QC_SCHEMA.missing, domain=None, range=Optional[int])

slots.missing_object_namespaces = Slot(uri=SCHEMA.missing_object_namespaces, name="missing_object_namespaces", curie=SCHEMA.curie('missing_object_namespaces'),
                   model_uri=MONARCH_KG_QC_SCHEMA.missing_object_namespaces, domain=None, range=Optional[Union[str, List[str]]])

slots.missing_objects = Slot(uri=MONARCH_KG_QC_SCHEMA.missing_objects, name="missing_objects", curie=MONARCH_KG_QC_SCHEMA.curie('missing_objects'),
                   model_uri=MONARCH_KG_QC_SCHEMA.missing_objects, domain=None, range=Optional[int])

slots.missing_subject_namespaces = Slot(uri=SCHEMA.missing_subject_namespaces, name="missing_subject_namespaces", curie=SCHEMA.curie('missing_subject_namespaces'),
                   model_uri=MONARCH_KG_QC_SCHEMA.missing_subject_namespaces, domain=None, range=Optional[Union[str, List[str]]])

slots.missing_subjects = Slot(uri=MONARCH_KG_QC_SCHEMA.missing_subjects, name="missing_subjects", curie=MONARCH_KG_QC_SCHEMA.curie('missing_subjects'),
                   model_uri=MONARCH_KG_QC_SCHEMA.missing_subjects, domain=None, range=Optional[int])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MONARCH_KG_QC_SCHEMA.name, domain=None, range=Optional[str])

slots.namespaces = Slot(uri=SCHEMA.namespaces, name="namespaces", curie=SCHEMA.curie('namespaces'),
                   model_uri=MONARCH_KG_QC_SCHEMA.namespaces, domain=None, range=Optional[Union[str, List[str]]])

slots.node_types = Slot(uri=SCHEMA.node_types, name="node_types", curie=SCHEMA.curie('node_types'),
                   model_uri=MONARCH_KG_QC_SCHEMA.node_types, domain=None, range=Optional[Union[Union[dict, NodeTypeReport], List[Union[dict, NodeTypeReport]]]])

slots.predicates = Slot(uri=SCHEMA.predicates, name="predicates", curie=SCHEMA.curie('predicates'),
                   model_uri=MONARCH_KG_QC_SCHEMA.predicates, domain=None, range=Optional[Union[Union[dict, PredicateReport], List[Union[dict, PredicateReport]]]])

slots.taxon = Slot(uri=SCHEMA.taxon, name="taxon", curie=SCHEMA.curie('taxon'),
                   model_uri=MONARCH_KG_QC_SCHEMA.taxon, domain=None, range=Optional[Union[str, List[str]]])

slots.total_number = Slot(uri=MONARCH_KG_QC_SCHEMA.total_number, name="total_number", curie=MONARCH_KG_QC_SCHEMA.curie('total_number'),
                   model_uri=MONARCH_KG_QC_SCHEMA.total_number, domain=None, range=Optional[int])

slots.uri = Slot(uri=SCHEMA.uri, name="uri", curie=SCHEMA.curie('uri'),
                   model_uri=MONARCH_KG_QC_SCHEMA.uri, domain=None, range=Optional[str])

slots.report__dangling_edges = Slot(uri=MONARCH_KG_QC_SCHEMA.dangling_edges, name="report__dangling_edges", curie=MONARCH_KG_QC_SCHEMA.curie('dangling_edges'),
                   model_uri=MONARCH_KG_QC_SCHEMA.report__dangling_edges, domain=None, range=Optional[Union[Union[dict, EdgeReport], List[Union[dict, EdgeReport]]]])

slots.report__edges = Slot(uri=MONARCH_KG_QC_SCHEMA.edges, name="report__edges", curie=MONARCH_KG_QC_SCHEMA.curie('edges'),
                   model_uri=MONARCH_KG_QC_SCHEMA.report__edges, domain=None, range=Optional[Union[Union[dict, EdgeReport], List[Union[dict, EdgeReport]]]])

slots.report__nodes = Slot(uri=MONARCH_KG_QC_SCHEMA.nodes, name="report__nodes", curie=MONARCH_KG_QC_SCHEMA.curie('nodes'),
                   model_uri=MONARCH_KG_QC_SCHEMA.report__nodes, domain=None, range=Optional[Union[Union[dict, NodeReport], List[Union[dict, NodeReport]]]])

slots.report__missing_nodes = Slot(uri=MONARCH_KG_QC_SCHEMA.missing_nodes, name="report__missing_nodes", curie=MONARCH_KG_QC_SCHEMA.curie('missing_nodes'),
                   model_uri=MONARCH_KG_QC_SCHEMA.report__missing_nodes, domain=None, range=Optional[Union[Union[dict, NodeReport], List[Union[dict, NodeReport]]]])