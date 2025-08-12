<figure>
  <img src="figures/BEAR.png" style="max-width: 100%; height: auto;" alt="BEAR Framework with Realizable Entities" />
</figure>

# BEAR: Value-First Ontology Engineering Framework 

High-quality ontology engineering traditionally prioritizes complete, reusable domain models. While effective
for broad reuse, this “ontology-first” approach can misalign with the needs of strategic decision makers, who
need targeted, actionable insights on constrained timelines. This paper introduces a value-first framework that
inverts this process, beginning with the strategic goals, jobs, and knowledge gaps of business leaders to generate
lean, purpose-built knowledge graph that delivers immediate value. In a pilot project with CompanyA, we
applied this framework to the wind energy ecosystem, successfully answering 15 distinct knowledge questions.
To demonstrate this, we focus on one such question out of 15, analyzing data from 35 companies collected
at WindEnergy Hamburg 2024. Our findings show that this approach not only answers knowledge questions
effectively through tailored visualizations but also uncovers critical blind spots—such as the intermediary roles of
consulting firms—that conventional business ecosystem analyses would necessarily miss.
 
# For the knowledge graph and data used in this study:

Look at KG&Data folder. It contains the knowledge graph in RDF format with WindEnergy Hamburg 2024 data (35 companies) for 10 distinct knowledge questions. Download the repository and open the rdf file in any RDF viewer, such as [Protégé].

If you want to see the inferences, protege does not direclty support visual blank node inferences, however, you can either use [GraphDB] and extract results with the queries, or you can use DL Query Tab in [Protégé] to see the inferences.

It is also interesting to see the individual tab, where you can see the individual blank nodes, however it is not possible to integrate new ones with the [Protégé] interface.

# To replicate the visualized results from the paper, follow these exact steps:
1. Go to the [VizLink](https://t-z-n.github.io/BusinessEcosystemVisualizer123/)
2. Select the granularity level +-1 from the left sidebar
3. Select the granularity level 5 from the top-left sidebar
4. Filter to Organization 7 and Organizaton 11

Uploaded visualization is the prototype version, therefore if bug occurs, please refresh the page.

# Repository Overview 📂

This repository contains the tools, data, and resources for applying the BEAR Framework:

- **📊 Figures**: Diagrams and illustrations of the BEAR Framework
  - `BEAR.png`: Visual representation of the framework's architecture

- **🔄 KG**: Knowledge Graph
  - `KG.rdf`: Knowledge graph in RDF format containing WindEnergy Hamburg 2024 data (37 survey responses, 35 companies) for 10 distinct knowledge questions.

- **🎯 OntologForum2025PresentationFiles**: Presentation materials from Ontology Summit 2025 
  - `Presentation.pdf`: Slides from the presentation "Beyond Blind Spots"

- **❓ Queries/**: Sample SPARQL queries
  - `Querry1.rq`, `Querry2.rq`: Example queries to extract insights from the knowledge graph, based on the paper's knowledge question.

- **📝 Survey**: Data Collection Methodology
  - `survey.pdf`: Survey template for WindEnergy Hamburg 2024

# Talks & Publications 🎓

## 📢 Talks relevant to BEAR
- Ontology Summit 2025: "Beyond Blind Spots: How Semantic Strategies Reveal Hidden Insights in the Business World"

# Future Work

- Integrating LLM within the architecture
- Graph Algorithms for pattern recognition

📧 Contact
Alican Tüzün - alican.tuezuen@fh-steyr.at