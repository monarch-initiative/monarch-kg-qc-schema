

CREATE TABLE "EdgeReport" (
	categories TEXT, 
	description TEXT, 
	name TEXT, 
	namespaces TEXT, 
	total_number INTEGER, 
	missing INTEGER, 
	node_types TEXT, 
	predicates TEXT, 
	PRIMARY KEY (categories, description, name, namespaces, total_number, missing, node_types, predicates)
);

CREATE TABLE "NodeReport" (
	categories TEXT, 
	description TEXT, 
	name TEXT, 
	namespaces TEXT, 
	total_number INTEGER, 
	taxon TEXT, 
	PRIMARY KEY (categories, description, name, namespaces, total_number, taxon)
);

CREATE TABLE "NodeTypeReport" (
	categories TEXT, 
	description TEXT, 
	name TEXT, 
	namespaces TEXT, 
	total_number INTEGER, 
	taxon TEXT, 
	missing INTEGER, 
	PRIMARY KEY (categories, description, name, namespaces, total_number, taxon, missing)
);

CREATE TABLE "PredicateReport" (
	missing_object_namespaces TEXT, 
	missing_objects INTEGER, 
	missing_subject_namespaces TEXT, 
	missing_subjects INTEGER, 
	total_number INTEGER, 
	uri TEXT, 
	PRIMARY KEY (missing_object_namespaces, missing_objects, missing_subject_namespaces, missing_subjects, total_number, uri)
);

CREATE TABLE "Report" (
	dangling_edges TEXT, 
	edges TEXT, 
	nodes TEXT, 
	missing_nodes TEXT, 
	PRIMARY KEY (dangling_edges, edges, nodes, missing_nodes)
);

CREATE TABLE "SubReport" (
	categories TEXT, 
	description TEXT, 
	name TEXT, 
	namespaces TEXT, 
	total_number INTEGER, 
	PRIMARY KEY (categories, description, name, namespaces, total_number)
);
