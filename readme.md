<figure>
  <img src="figures/BEAR.png" style="max-width: 100%; height: auto;" alt="BEAR Framework with Realizable Entities" />
</figure>

# BEAR: Value-Driven Ontology Engineering Framework for Business Ecosystem Analysis and Representation

Traditional business ecosystem analysis often overlooks structural complexities, creating blind spots. While ontology and knowledge graph engineering (OKGE) offer powerful frameworks for revealing these complexities, their contextual utility is undermined by neglecting the core business concept, the value. To bridge this gap, this short paper introduces the Business Ecosystem Analysis and Representation (BEAR) framework, a value-driven semantic approach. BEAR begins by capturing stakeholder goals, jobs-to-be-done, and knowledge gaps, and formulates them as knowledge questions for creating a foundation for OKGE. This initial focus ensures OKGE delivers strategic value with tailored visualizations as an answering mechanism. We applied BEAR to the wind energy ecosystem to show this approach, analyzing data from 35 companies collected at WindEnergy Hamburg 2024 as an initial demonstration. Our preliminary findings show that BEAR effectively guided answering stakeholders' knowledge questions through tailored visualizations and uncovered strategic blind spots (e.g., intermediary roles) that conventional non-semantic analyses would likely miss.
 
# For the knowledge graph and data used in this study:

Look at KG&Data folder. It contains the knowledge graph in RDF format with WindEnergy Hamburg 2024 data (35 companies). Anonymized github can be bugged, you just need to download the repository and open the rdf file in any RDF viewer, such as [Protégé].

If you want to see the inferences, protege does not direclty support visual blank node inferences, however, you can either use [GraphDB] and extract results with the queries, or you can use DL Query Tab in [Protégé] to see the inferences.

It is also interesting to see the individual tab, where you can see the individual blank nodes, however it is not possible to integrate new ones with the [Protégé] interface.

# To replicate the visualized results from the paper, follow these exact steps:
1. Go to the [VizLink](https://anonymous.4open.science/w/BusinessEcosystemVisualizer123-09FD/)
2. Select the granularity level +-1 from the left sidebar
3. Select the granularity level 5 from the top-left sidebar
4. Filter to Organization 7 and Organizaton 11

Sometimes link does not work properly due to Github Anonymizer, so please refresh the page if you encounter issues.

Uploaded visualization is the prototype version, therefore if bug occurs, please refresh the page.

# Repository Overview 📂

This repository contains the tools, data, and resources for applying the BEAR Framework:

- **📊 Figures**: Diagrams and illustrations of the BEAR Framework
  - `BEAR.png`: Visual representation of the framework's architecture

- **🔄 KG&Data**: Knowledge Graph and Dataset
  - `KG.rdf`: Knowledge graph in RDF format containing WindEnergy Hamburg 2024 data (35 companies)

- **🎯 OntologForum2025PresentationFiles**: Presentation materials from Ontology Summit 2025 
  - `Presentation.pdf`: Slides from the presentation "Beyond Blind Spots"

- **❓ Queries/**: Sample SPARQL queries
  - `Querry1.rq`, `Querry2.rq`: Example queries to extract insights from the knowledge graph

- **📝 Survey**: Data Collection Methodology
  - `survey.pdf`: Survey template for WindEnergy Hamburg 2024

# Talks & Publications 🎓

## 📢 Talks
- Ontology Summit 2025: "Beyond Blind Spots: How Semantic Strategies Reveal Hidden Insights in the Business World"


# Future Work

- Integrating LLM within the architecture
- Graph Algorithms for pattern recognition
