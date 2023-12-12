

/**
 * Represents a Report
 */
export interface Report {
    /** Report summarizing knowledge graph dangling edges */
    dangling_edges?: EdgeReport,
    /** Report summarizing knowledge graph edges */
    edges: EdgeReport,
    /** Report summarizing knowledge graph nodes */
    nodes: NodeReport,
    /** Report summarizing knowledge graph missing nodes */
    missing_nodes?: NodeReport,
};
/**
 * An abstract report section for a knowledge graph
 */
export interface SubReport {
    /** The categories of the node or edge objects */
    categories?: string[],
    /** A human-readable description for a thing */
    description?: string,
    /** A human-readable name for a thing */
    name?: string,
    /** The namespaces of the node or edge objects */
    namespaces?: string[],
    /** Total number of edge or node objects */
    total_number?: number,
};
/**
 * A sub report summarizing a collection of edges
 */
export interface EdgeReport extends SubReport {
    /** Number of missing of type in collection */
    missing?: number,
    /** NodeType reports for the edges collection */
    node_types?: NodeTypeReport[],
    /** Predicate reports for the edges collection */
    predicates?: PredicateReport[],
    /** The categories of the node or edge objects */
    categories?: string[],
    /** A human-readable description for a thing */
    description?: string,
    /** A human-readable name for a thing */
    name?: string,
    /** The namespaces of the node or edge objects */
    namespaces?: string[],
    /** Total number of edge or node objects */
    total_number?: number,
};
/**
 * A sub report summarizing a collection of nodes
 */
export interface NodeReport extends SubReport {
    /** The taxons of the nodes in the collection */
    taxon?: string[],
    /** The categories of the node or edge objects */
    categories?: string[],
    /** A human-readable description for a thing */
    description?: string,
    /** A human-readable name for a thing */
    name?: string,
    /** The namespaces of the node or edge objects */
    namespaces?: string[],
    /** Total number of edge or node objects */
    total_number?: number,
};
/**
 * A sub report summarizing the types of a collection of nodes
 */
export interface NodeTypeReport extends NodeReport {
    /** Number of missing of type in collection */
    missing?: number,
    /** The taxons of the nodes in the collection */
    taxon?: string[],
    /** The categories of the node or edge objects */
    categories?: string[],
    /** A human-readable description for a thing */
    description?: string,
    /** A human-readable name for a thing */
    name?: string,
    /** The namespaces of the node or edge objects */
    namespaces?: string[],
    /** Total number of edge or node objects */
    total_number?: number,
};
/**
 * A sub report summarizing the predicates of a collection
 */
export interface PredicateReport {
    /** Namespaces of missing objects from predicate edges collection */
    missing_object_namespaces?: string[],
    /** Number of missing objects in edges of predicate collection */
    missing_objects?: number,
    /** Namespaces of mission subjects from predicate edges collection */
    missing_subject_namespaces?: string[],
    /** Number of mission subjects in edges of predicate collection */
    missing_subjects?: number,
    /** Total number of edge or node objects */
    total_number?: number,
    /** Predicate URI for the group of edges */
    uri?: string,
};

