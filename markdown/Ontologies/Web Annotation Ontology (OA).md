### Web Annotation Ontology <a name="web-annotation-ontology" />
[OA][OA] [TTL][OA-TTL] [DOC][OA-DOC]

An ontology for describing web annotations. "Typically an Annotation has a single Body, which is the comment or other descriptive resource, and a single Target that the Body is somehow "about". The Body provides the information which is annotating the Target."

![Relationship between annotation, body, and target](http://www.openannotation.org/spec/core/images/intro_model.png)

#### Annotation class
Has two required predicates:
* *oa:hasTarget*: The source, document, page, etc. that the annotation corresponds to. The target can be further specified by a selector which has an *oa:start* and an *oa:end*

![How to use the text selector](https://www.w3.org/TR/annotation-vocab/images/examples/textPositionSelector.png)

* *rdf:type*: In this case, the type of annotation is *oa:Annotation*

And four recommended predicates:
* *oa:hasBody*: The entity, or content of the annotation
* *oa:motivatedBy*: Reason for creating th annotation
* *dcterms:creator*: The person who created the annotation, the annotator
* *dcterms:created*: The date/time of of the creation of the annotation


![Annotation class](https://www.w3.org/TR/annotation-vocab/images/examples/annotation.png)

***

[OA]: https://www.w3.org/ns/oa
[OA-TTL]: http://www.w3.org/ns/oa.ttl
[OA-DOC]: https://www.w3.org/TR/annotation-vocab/


