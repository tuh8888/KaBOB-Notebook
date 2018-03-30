### Gene Ontology <a name="gene-ontology" />
[GO][GO] [OWL][GO-OWL] [DOC] [GO-DOC]
(Note: GO-Plus is the version in KaBOB)

A set of three ontologies that describe gene functions. They are is_a disjoint, but other types of relationships do span the ontologies. Cross products (definition by combining other terms) is contained in the *intersection_of* lines.

#### Subontologies
* Biological process: The larger proecesses, or 'biological programs', accomplished by multiple molecular activities. Must have more than one distinct step. Does not attepmt to fully describe pathways

* Molecular function: Molecular level activities performed by gene products.
    * Represent activities rather than the entities that perform the actions.
    * Usually end with the word "activity"

* Cellular component: The locations relative to cellular structures in which a gene product performs a function. Biologists describe the locations of gene products in two ways:
    * 1. Relative to cellular structures or compartments
    * 2. The stable macromolecular complexes of which they are the parts

#### [Relations][GO-Relations]

* *is_a*: subtype of
    * Transitive: if A *is a* B, and B *is a* C, then A *is a* C
* *part_of*
* *has_part*
* *regulates*
* *negatively_regulates*
* *positively_regulates*

![Diagram of the GO](http://www.geneontology.org/sites/default/files/u425/diag-ontology-graph.gif)

***

[GO]: http://www.geneontology.org/
[GO-OWL]: http://purl.obolibrary.org/obo/go.owl
[GO-DOC]: http://www.geneontology.org/page/ontology-documentation
[GO-Relations]: http://www.geneontology.org/page/ontology-relations

