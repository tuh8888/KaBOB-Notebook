### Protein Ontology <a name="protein-ontology" />
[PRO][PRO] [OWL][PR-OWL] [DOC][PRO-DOC]
(Note: Not sure if PR and PRO are the same. PR is in KaBOB)

#### Sub-Ontologies
* ProEvo: Evolutionary relatedness
    * Proteins from different but related (orthalogous or paralogous) genes
    * Strictly *is_a* relations
* ProForm: Protein forms produced from a given gene locus
    * All splice isoform, mutant variant, or post/co-translationally modified forms
    * *is_a* and *derives_from* relations
* ProComp: Protein-containing complexes
    * Uses only *is_a* but complexes *have_part* subunits

![PRO Schema](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3013777/bin/gkq907f1.jpg)

***

[PRO]: https://pir.georgetown.edu/pro/pro.shtml
[PR-OWL]: http://purl.obolibrary.org/obo/pr.owl
[PRO-DOC]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3013777/

