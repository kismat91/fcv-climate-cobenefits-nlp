############################################################
# PROMPTS
############################################################
PROMPT_1 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a Yes, Partial, or No response for each question and provide a detailed analysis to justify your choice.
Scoring System:
•	Yes = The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.
•	Partial = The PAD references the issue but in a limited, superficial, or indirect way, or lacks full coverage.
•	No = There is no evidence in the PAD that the issue has been addressed.
Output Format:
For each characteristic, provide the following:
1.	Guiding Question: [Question]
o	Analysis: [Detailed analysis of how the PAD addresses the question]
o	Score: [Yes/Partial/No]
At the end, provide:
•	Overall FCV Sensitivity Assessment: [Summary of how well the PAD integrates FCV-sensitive measures]
Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]
2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
o	Analysis: [Your analysis here]
o	Score: [Yes/Partial/No]

Overall FCV Sensitivity Assessment
Summary: [Brief summary of how well the PAD integrates FCV-sensitive measures, highlighting strengths and weaknesses]


"""

PROMPT_2 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.
Scoring System:
•	9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
•	6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
•	3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
•	0-2 = Not Addressed: No reference to FCV-related risks or considerations.
Output Format:
For each characteristic, provide the following:
1.	Guiding Question: [Question]
o	Analysis: [Detailed analysis of how the PAD addresses the question]
o	Score: [Score between 0 and 10]
o	Running sum: [Sum of scores for questions till now]
At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]
Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Overall FCV Sensitivity Score
•	Total Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_3 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) using the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-100) for each question and provide a detailed analysis to justify your score.
Scoring System:
•	90-100 = Exceptional: Comprehensive FCV integration with detailed risk analysis and mitigation strategies.
•	75-89 = Strong: Well-addressed but may have some gaps in FCV consideration.
•	50-74 = Moderate: References FCV risks but lacks full integration or depth.
•	25-49 = Weak: Limited or indirect mention of FCV factors with minimal strategy.
•	0-24 = Not Addressed: No mention of FCV issues in the PAD.
Output Format:
For each characteristic, provide the following:
1.	Guiding Question: [Question]
o	Analysis: [Detailed analysis of how the PAD addresses the question]
o	Score: [0-100]
At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]
Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
o	Analysis: [Your analysis here]
o	Score: [0-100]
2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
o	Analysis: [Your analysis here]
o	Score: [0-100]
Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
o	Analysis: [Your analysis here]
o	Score: [0-100]
2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
o	Analysis: [Your analysis here]
o	Score: [0-100]
3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
o	Analysis: [Your analysis here]
o	Score: [0-100]
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
o	Analysis: [Your analysis here]
o	Score: [0-100]
2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
o	Analysis: [Your analysis here]
o	Score: [0-100]
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
o	Analysis: [Your analysis here]
o	Score: [0-100]
2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
o	Analysis: [Your analysis here]
o	Score: [0-100]
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
o	Analysis: [Your analysis here]
o	Score: [0-100]
2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
o	Analysis: [Your analysis here]
o	Score: [0-100]
Overall FCV Sensitivity Score
•	Total Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_4 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Scoring System:

3 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.

2 = Moderately Addressed: The PAD adequately addresses the question but may lack depth or completeness.

1 = Weakly Addressed: The PAD references the issue but in a limited, superficial, or indirect way.

0 = Not Addressed: There is no evidence in the PAD that the issue has been addressed.

Output Format:

For each characteristic, provide the following:

Guiding Question: [Question]

Analysis: [Detailed analysis of how the PAD addresses the question]

Score: [Score between 0 and 3]

Running sum: [Sum of scores for questions till now]

At the end, provide:

Overall FCV Sensitivity Score: [Sum of scores for all questions]

Summary: [Brief summary of the PAD's FCV sensitivity]

Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?

Analysis: [Your analysis here()]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score

Total Score: [Sum of scores for all questions]

Summary: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]


"""

PROMPT_5 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Scoring System:
3 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.
2 = Moderately Addressed: The PAD adequately addresses the question but may lack depth or completeness.
1 = Weakly Addressed: The PAD references the issue but in a limited, superficial, or indirect way.
0 = Not Addressed: There is no evidence in the PAD that the issue has been addressed.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Score: [Score between 0 and 3]

At the end, provide:
Overall FCV Sensitivity Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD's FCV sensitivity]

Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Core Issues to Consider: This question evaluates whether the PAD anticipates and addresses FCV-related risks that might disrupt the project. Relevant traits include identifying barriers such as insecurity, governance deficits, corruption, or social mistrust, which can impede delivery. Look for explicit acknowledgment of risks in areas like service delivery, stakeholder engagement, or operational access.
High vs. Low Scores: A high score reflects clearly identified risks, with detailed mitigation strategies such as capacity-building for weak institutions or contingency plans for conflict-prone areas. A low score reflects minimal or superficial identification of FCV risks, with no evidence of how these might impact implementation or how they would be mitigated. 
Key Sections to Review: The Key Risks and Implementation Arrangements sections.
Analysis: [Your analysis here]
Score: [0-3]

Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Core Issues to Consider: This question assesses whether the PAD explains how climate-related risks (e.g., floods, droughts, storms) exacerbate or intersect with drivers of fragility, conflict, and violence (FCV). Discussions should highlight how resource scarcity, governance challenges, or displacement may emerge or worsen due to climate impacts. The PAD should provide evidence-based, context-specific analysis.
High vs. Low Scores: A high score reflects a detailed and localized analysis of climate-FCV interactions, linking specific climate risks to governance failures, social inequalities, or resource disputes. A low score indicates either a lack of analysis or only generic references to climate-FCV interactions. 
Key Sections to Review: The Country Context and Sectoral and Institutional Context sections.
Analysis: [Your analysis here]
Score: [0-3]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Core Issues to Consider: This question examines whether the project design includes safeguards to prevent unintended consequences that could increase fragility, such as competition over resources, exclusion of vulnerable groups, or reinforcing local inequalities.
High vs. Low Scores: A high score reflects a well-developed safeguards framework, including measures like conflict-sensitive programming and community engagement. A low score suggests limited or no discussion of safeguards to prevent harm.
Key Sections to Review: Safeguards, Key Risks and Mitigation Measures
Analysis: [Your analysis here]
Score: [0-3]

Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Core Issues to Consider: Projects in FCV settings require flexibility to adjust to changing security, political, or environmental conditions. Look for contingency plans, flexible funding mechanisms, and iterative project adjustments.
High vs. Low Scores: A high score reflects clear mechanisms for adaptability, such as scenario planning or dynamic project components. A low score suggests rigidity in project design with no adaptability measures.
Key Sections to Review: Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, Sustainability
Analysis: [Your analysis here]
Score: [0-3]

Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Core Issues to Consider: This question assesses whether the PAD takes a balanced approach to addressing urgent climate-related needs (e.g., disaster response, humanitarian aid) while ensuring long-term resilience (e.g., sustainable infrastructure, capacity-building). Maladaptation occurs when short-term measures (e.g., temporary flood barriers, rapid deforestation for agricultural expansion) create vulnerabilities that increase future risks.
High vs. Low Scores: A high score reflects a well-integrated approach where interventions are designed for both immediate relief and long-term sustainability, with explicit risk assessments and mitigation strategies. A low score reflects a lack of foresight, where short-term actions may unintentionally worsen vulnerabilities or fail to align with long-term development goals.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Sustainability
Analysis: [Your analysis here]
Score: [0-3]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Core Issues to Consider: Projects should aim to reduce fragility by tackling governance challenges, improving resource management, and strengthening institutions.
High vs. Low Scores: A high score reflects targeted interventions to address FCV root causes, while a low score suggests no consideration of these factors.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Project Components
Analysis: [Your analysis here]
Score: [0-3]

Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Core Issues to Consider: This question examines whether the PAD integrates peacebuilding efforts into its climate interventions. Effective projects in FCV settings should not only mitigate environmental risks but also address social and political tensions that contribute to conflict. Examples include participatory decision-making, community dispute resolution mechanisms, and ensuring marginalized groups are included in governance structures.
High vs. Low Scores: A high score reflects intentional peacebuilding elements, such as inclusive governance mechanisms, conflict-sensitive resource management, or dialogue facilitation. A low score lacks any consideration of how the project may influence or mitigate social tensions.
Key Sections to Review: Higher-Level Objectives to Which the Project Contributes, Safeguards, Key Risks and Mitigation Measures, Institutional and Implementation Arrangements
Analysis: [Your analysis here]
Score: [0-3]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Core Issues to Consider: Projects should incorporate equity considerations and ensure vulnerable groups are not left behind.
High vs. Low Scores: A high score reflects strong provisions for inclusivity and targeted support for vulnerable groups. A low score lacks consideration for marginalized populations.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Social (including Safeguards), Project Beneficiaries
Analysis: [Your analysis here]
Score: [0-3]

Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Core Issues to Consider: This question evaluates whether the project actively ensures that benefits (e.g., resources, infrastructure, economic opportunities) are fairly distributed across different social groups, particularly in fragile and conflict-affected settings. Without careful planning, projects can unintentionally exacerbate existing inequalities by favoring certain regions, ethnic groups, or social classes.
High vs. Low Scores: A high score reflects proactive measures such as social impact assessments, grievance mechanisms, and affirmative actions to support marginalized communities. A low score indicates a lack of safeguards, risking uneven benefits distribution and potential conflicts.
Key Sections to Review: Higher-Level Objectives to Which the Project Contributes, Project Components, Key Risks and Mitigation Measures, Results Framework and Monitoring
Analysis: [Your analysis here]
Score: [0-3]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Core Issues to Consider: Collaboration among multiple actors ensures a holistic approach to FCV-sensitive climate action. Look for evidence of joint planning and partnerships.
High vs. Low Scores: A high score reflects well-documented partnerships with key actors. A low score lacks discussion of intersectoral collaboration.
Key Sections to Review: Sectoral and Institutional Context, Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, Implementation Support Plan
Analysis: [Your analysis here]
Score: [0-3]

Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Core Issues to Consider: This question assesses whether the project ensures alignment and coordination across multiple stakeholders, including government agencies, development organizations, humanitarian actors, and local institutions. Poor coordination can lead to inefficiencies, conflicting mandates, or duplication of efforts, undermining project effectiveness.
High vs. Low Scores: A high score reflects clear mechanisms for coordination, such as joint working groups, formal agreements, or integrated planning frameworks. A low score indicates fragmented planning, where stakeholders work in silos without effective collaboration.
Key Sections to Review: Institutional and Implementation Arrangements, Project Components, Key Risks and Mitigation Measures, Results Framework and Monitoring
Analysis: [Your analysis here]
Score: [0-3]


Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_4_IMP = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Scoring System:

3 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.

2 = Moderately Addressed: The PAD adequately addresses the question but may lack depth or completeness.

1 = Weakly Addressed: The PAD references the issue but in a limited, superficial, or indirect way.

0 = Not Addressed: There is no evidence in the PAD that the issue has been addressed.

Output Format:

For each characteristic, provide the following:

Guiding Question: [Question]

Analysis: [Detailed analysis of how the PAD addresses the question]

Score: [Score between 0 and 3]

Running sum: [Sum of scores for questions till now]

At the end, provide:

Overall FCV Sensitivity Score: [Sum of scores for all questions]

Summary: [Brief summary of the PAD's FCV sensitivity]

The below are the sections that are likely to be of greatest interest:

- Country Context
- Sectoral and Institutional Context
- Project Components
- Project Beneficiaries
- Rationale for Bank Involvement
- Key Risks
- Sustainability
- Environmental and Social Risk Analysis
- Stakeholder Engagement Plan (SEP)
- Implementation Arrangements

Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?

Analysis: [Your analysis here()]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?

Analysis: [Your analysis here]

Score: [0-3]

Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score

Total Score: [Sum of scores for all questions]

Summary: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]


"""

PROMPT_2_IMP = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.
Scoring System:
•	9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
•	6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
•	3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
•	0-2 = Not Addressed: No reference to FCV-related risks or considerations.
Output Format:
For each characteristic, provide the following:
1.	Guiding Question: [Question]
o	Analysis: [Detailed analysis of how the PAD addresses the question]
o	Score: [Score between 0 and 10]
o	Running sum: [Sum of scores for questions till now]
At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]
The below are the sections that are likely to be of greatest interest:
- Country Context
- Sectoral and Institutional Context
- Project Components
- Project Beneficiaries
- Rationale for Bank Involvement
- Key Risks
- Sustainability
- Environmental and Social Risk Analysis
- Stakeholder Engagement Plan (SEP)
- Implementation Arrangements
Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
o	Analysis: [Your analysis here]
o	Score: [0-10]
o	Running sum: [Sum of scores for questions till now]
Overall FCV Sensitivity Score
•	Total Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_2_LOGG_1 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.

Scoring System:
9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
0-2 = Not Addressed: No reference to FCV-related risks or considerations.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: (Ensure that the sum equals 1) (give an array of probabilities for all possible scores with their corresponding scores like below, only if probability is more than 0)
- x(score): [probability of getting x score] 
Log Probabilities: (Calculate as natural logarithm of probability, only if probability is more than 0) (give an array of log of probabilities for each score upto 2 digit precision)
- x(score): ln([probability of getting x score])
Score: [Score between 0 and 10, which has the highest probability]
Running Sum: [Sum of scores for questions till now]

At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]

Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]


Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

(Ensure that the sum of probabilities across all possible scores for each question is always equal to 1)

"""

PROMPT_2_LOGG_2 = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.

Scoring System:
9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
0-2 = Not Addressed: No reference to FCV-related risks or considerations.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: (Ensure that the sum equals 1) (give an array of probabilities for all possible scores with their corresponding scores like below, only if probability is more than 0)
- x(score): [probability of getting x score] 
Log Probabilities: (Calculate as natural logarithm of probability, only if probability is more than 0) (give an array of log of probabilities for each score upto 2 digit precision)
- x(score): ln([probability of getting x score])
Score: [Score between 0 and 10, which has the highest probability]
Running Sum: [Sum of scores for questions till now]

At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]

Evaluation Criteria
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

(Ensure that the sum of probabilities across all possible scores for each question is always equal to 1)

"""


# Prompts with log probabilities

PROMPT_4_LOG = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Scoring System:
3 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.
2 = Moderately Addressed: The PAD adequately addresses the question but may lack depth or completeness.
1 = Weakly Addressed: The PAD references the issue but in a limited, superficial, or indirect way.
0 = Not Addressed: There is no evidence in the PAD that the issue has been addressed.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Log Probabilites: score 0 [log probability], score 1 [log probability], score 2 [log probability], score 3 [log probability]
Score: [Score between 0 and 3]
Running sum: [Sum of scores for questions till now]

At the end, provide:
Overall FCV Sensitivity Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD's FCV sensitivity]

Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]
"""

PROMPT_2_LOG = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.

Scoring System:
•	9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
•	6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
•	3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
•	0-2 = Not Addressed: No reference to FCV-related risks or considerations.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities (Make sure sum is 1): score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability], score 4 [probability], score 5 [probability], score 6 [probability], score 7 [probability], score 8 [probability], score 9 [probability], score 10 [probability]
Log Probabilites: score 0 [log probability], score 1 [log probability], score 2 [log probability], score 3 [log probability], score 4 [log probability], score 5 [log probability], score 6 [log probability], score 7 [log probability], score 8 [log probability], score 9 [log probability], score 10 [log probability]
Score: [Score between 0 and 10]
Running sum: [Sum of scores for questions till now]

At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]

Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_4_IMP_LOG = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Scoring System:
3 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.
2 = Moderately Addressed: The PAD adequately addresses the question but may lack depth or completeness.
1 = Weakly Addressed: The PAD references the issue but in a limited, superficial, or indirect way.
0 = Not Addressed: There is no evidence in the PAD that the issue has been addressed.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Log Probabilites: score 0 [log probability], score 1 [log probability], score 2 [log probability], score 3 [log probability]
Score: [Score between 0 and 3]
Running sum: [Sum of scores for questions till now]

At the end, provide:
Overall FCV Sensitivity Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD's FCV sensitivity]

Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Core Issues to Consider: This question evaluates whether the PAD anticipates and addresses FCV-related risks that might disrupt the project. Relevant traits include identifying barriers such as insecurity, governance deficits, corruption, or social mistrust, which can impede delivery. Look for explicit acknowledgment of risks in areas like service delivery, stakeholder engagement, or operational access.
High vs. Low Scores: A high score reflects clearly identified risks, with detailed mitigation strategies such as capacity-building for weak institutions or contingency plans for conflict-prone areas. A low score reflects minimal or superficial identification of FCV risks, with no evidence of how these might impact implementation or how they would be mitigated. 
Key Sections to Review: The Key Risks and Implementation Arrangements sections.
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Core Issues to Consider: This question assesses whether the PAD explains how climate-related risks (e.g., floods, droughts, storms) exacerbate or intersect with drivers of fragility, conflict, and violence (FCV). Discussions should highlight how resource scarcity, governance challenges, or displacement may emerge or worsen due to climate impacts. The PAD should provide evidence-based, context-specific analysis.
High vs. Low Scores: A high score reflects a detailed and localized analysis of climate-FCV interactions, linking specific climate risks to governance failures, social inequalities, or resource disputes. A low score indicates either a lack of analysis or only generic references to climate-FCV interactions. 
Key Sections to Review: The Country Context and Sectoral and Institutional Context sections.
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Core Issues to Consider: This question examines whether the project design includes safeguards to prevent unintended consequences that could increase fragility, such as competition over resources, exclusion of vulnerable groups, or reinforcing local inequalities.
High vs. Low Scores: A high score reflects a well-developed safeguards framework, including measures like conflict-sensitive programming and community engagement. A low score suggests limited or no discussion of safeguards to prevent harm.
Key Sections to Review: Safeguards, Key Risks and Mitigation Measures
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Core Issues to Consider: Projects in FCV settings require flexibility to adjust to changing security, political, or environmental conditions. Look for contingency plans, flexible funding mechanisms, and iterative project adjustments.
High vs. Low Scores: A high score reflects clear mechanisms for adaptability, such as scenario planning or dynamic project components. A low score suggests rigidity in project design with no adaptability measures.
Key Sections to Review: Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, Sustainability
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Core Issues to Consider: This question assesses whether the PAD takes a balanced approach to addressing urgent climate-related needs (e.g., disaster response, humanitarian aid) while ensuring long-term resilience (e.g., sustainable infrastructure, capacity-building). Maladaptation occurs when short-term measures (e.g., temporary flood barriers, rapid deforestation for agricultural expansion) create vulnerabilities that increase future risks.
High vs. Low Scores: A high score reflects a well-integrated approach where interventions are designed for both immediate relief and long-term sustainability, with explicit risk assessments and mitigation strategies. A low score reflects a lack of foresight, where short-term actions may unintentionally worsen vulnerabilities or fail to align with long-term development goals.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Sustainability
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Core Issues to Consider: Projects should aim to reduce fragility by tackling governance challenges, improving resource management, and strengthening institutions.
High vs. Low Scores: A high score reflects targeted interventions to address FCV root causes, while a low score suggests no consideration of these factors.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Project Components
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Core Issues to Consider: This question examines whether the PAD integrates peacebuilding efforts into its climate interventions. Effective projects in FCV settings should not only mitigate environmental risks but also address social and political tensions that contribute to conflict. Examples include participatory decision-making, community dispute resolution mechanisms, and ensuring marginalized groups are included in governance structures.
High vs. Low Scores: A high score reflects intentional peacebuilding elements, such as inclusive governance mechanisms, conflict-sensitive resource management, or dialogue facilitation. A low score lacks any consideration of how the project may influence or mitigate social tensions.
Key Sections to Review: Higher-Level Objectives to Which the Project Contributes, Safeguards, Key Risks and Mitigation Measures, Institutional and Implementation Arrangements
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Core Issues to Consider: Projects should incorporate equity considerations and ensure vulnerable groups are not left behind.
High vs. Low Scores: A high score reflects strong provisions for inclusivity and targeted support for vulnerable groups. A low score lacks consideration for marginalized populations.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Social (including Safeguards), Project Beneficiaries
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Core Issues to Consider: This question evaluates whether the project actively ensures that benefits (e.g., resources, infrastructure, economic opportunities) are fairly distributed across different social groups, particularly in fragile and conflict-affected settings. Without careful planning, projects can unintentionally exacerbate existing inequalities by favoring certain regions, ethnic groups, or social classes.
High vs. Low Scores: A high score reflects proactive measures such as social impact assessments, grievance mechanisms, and affirmative actions to support marginalized communities. A low score indicates a lack of safeguards, risking uneven benefits distribution and potential conflicts.
Key Sections to Review: Higher-Level Objectives to Which the Project Contributes, Project Components, Key Risks and Mitigation Measures, Results Framework and Monitoring
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Core Issues to Consider: Collaboration among multiple actors ensures a holistic approach to FCV-sensitive climate action. Look for evidence of joint planning and partnerships.
High vs. Low Scores: A high score reflects well-documented partnerships with key actors. A low score lacks discussion of intersectoral collaboration.
Key Sections to Review: Sectoral and Institutional Context, Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, Implementation Support Plan
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Core Issues to Consider: This question assesses whether the project ensures alignment and coordination across multiple stakeholders, including government agencies, development organizations, humanitarian actors, and local institutions. Poor coordination can lead to inefficiencies, conflicting mandates, or duplication of efforts, undermining project effectiveness.
High vs. Low Scores: A high score reflects clear mechanisms for coordination, such as joint working groups, formal agreements, or integrated planning frameworks. A low score indicates fragmented planning, where stakeholders work in silos without effective collaboration.
Key Sections to Review: Institutional and Implementation Arrangements, Project Components, Key Risks and Mitigation Measures, Results Framework and Monitoring
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-3]
Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_2_IMP_LOG = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.

Scoring System:
•	9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
•	6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
•	3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
•	0-2 = Not Addressed: No reference to FCV-related risks or considerations.

Output Format:
For each characteristic, provide the following:
1.	Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability], score 4 [probability], score 5 [probability], score 6 [probability], score 7 [probability], score 8 [probability], score 9 [probability], score 10 [probability]
Log Probabilites: score 0 [log probability], score 1 [log probability], score 2 [log probability], score 3 [log probability], score 4 [log probability], score 5 [log probability], score 6 [log probability], score 7 [log probability], score 8 [log probability], score 9 [log probability], score 10 [log probability]
Score: [Score between 0 and 10]
Running sum: [Sum of scores for questions till now]

At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]

Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Core Issues to Consider: This question evaluates whether the PAD anticipates and addresses FCV-related risks that might disrupt the project. Relevant traits include identifying barriers such as insecurity, governance deficits, corruption, or social mistrust, which can impede delivery. Look for explicit acknowledgment of risks in areas like service delivery, stakeholder engagement, or operational access.
High vs. Low Scores: A high score reflects clearly identified risks, with detailed mitigation strategies such as capacity-building for weak institutions or contingency plans for conflict-prone areas. A low score reflects minimal or superficial identification of FCV risks, with no evidence of how these might impact implementation or how they would be mitigated. 
Key Sections to Review: The Key Risks and Implementation Arrangements sections.
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Core Issues to Consider: This question assesses whether the PAD explains how climate-related risks (e.g., floods, droughts, storms) exacerbate or intersect with drivers of fragility, conflict, and violence (FCV). Discussions should highlight how resource scarcity, governance challenges, or displacement may emerge or worsen due to climate impacts. The PAD should provide evidence-based, context-specific analysis.
High vs. Low Scores: A high score reflects a detailed and localized analysis of climate-FCV interactions, linking specific climate risks to governance failures, social inequalities, or resource disputes. A low score indicates either a lack of analysis or only generic references to climate-FCV interactions. 
Key Sections to Review: The Country Context and Sectoral and Institutional Context sections.
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Core Issues to Consider: This question examines whether the project design includes safeguards to prevent unintended consequences that could increase fragility, such as competition over resources, exclusion of vulnerable groups, or reinforcing local inequalities.
High vs. Low Scores: A high score reflects a well-developed safeguards framework, including measures like conflict-sensitive programming and community engagement. A low score suggests limited or no discussion of safeguards to prevent harm.
Key Sections to Review: Safeguards, Key Risks and Mitigation Measures
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Core Issues to Consider: This question assesses whether the PAD takes a balanced approach to addressing urgent climate-related needs (e.g., disaster response, humanitarian aid) while ensuring long-term resilience (e.g., sustainable infrastructure, capacity-building). Maladaptation occurs when short-term measures (e.g., temporary flood barriers, rapid deforestation for agricultural expansion) create vulnerabilities that increase future risks.
High vs. Low Scores: A high score reflects a well-integrated approach where interventions are designed for both immediate relief and long-term sustainability, with explicit risk assessments and mitigation strategies. A low score reflects a lack of foresight, where short-term actions may unintentionally worsen vulnerabilities or fail to align with long-term development goals.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Sustainability
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Core Issues to Consider: Projects should aim to reduce fragility by tackling governance challenges, improving resource management, and strengthening institutions.
High vs. Low Scores: A high score reflects targeted interventions to address FCV root causes, while a low score suggests no consideration of these factors.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Project Components
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Core Issues to Consider: This question examines whether the PAD integrates peacebuilding efforts into its climate interventions. Effective projects in FCV settings should not only mitigate environmental risks but also address social and political tensions that contribute to conflict. Examples include participatory decision-making, community dispute resolution mechanisms, and ensuring marginalized groups are included in governance structures.
High vs. Low Scores: A high score reflects intentional peacebuilding elements, such as inclusive governance mechanisms, conflict-sensitive resource management, or dialogue facilitation. A low score lacks any consideration of how the project may influence or mitigate social tensions.
Key Sections to Review: Higher-Level Objectives to Which the Project Contributes, Safeguards, Key Risks and Mitigation Measures, Institutional and Implementation Arrangements
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Core Issues to Consider: Projects should incorporate equity considerations and ensure vulnerable groups are not left behind.
High vs. Low Scores: A high score reflects strong provisions for inclusivity and targeted support for vulnerable groups. A low score lacks consideration for marginalized populations.
Key Sections to Review: Country Context, Sectoral and Institutional Context, Social (including Safeguards), Project Beneficiaries
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Core Issues to Consider: This question evaluates whether the project actively ensures that benefits (e.g., resources, infrastructure, economic opportunities) are fairly distributed across different social groups, particularly in fragile and conflict-affected settings. Without careful planning, projects can unintentionally exacerbate existing inequalities by favoring certain regions, ethnic groups, or social classes.
High vs. Low Scores: A high score reflects proactive measures such as social impact assessments, grievance mechanisms, and affirmative actions to support marginalized communities. A low score indicates a lack of safeguards, risking uneven benefits distribution and potential conflicts.
Key Sections to Review: Higher-Level Objectives to Which the Project Contributes, Project Components, Key Risks and Mitigation Measures, Results Framework and Monitoring
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Core Issues to Consider: Collaboration among multiple actors ensures a holistic approach to FCV-sensitive climate action. Look for evidence of joint planning and partnerships.
High vs. Low Scores: A high score reflects well-documented partnerships with key actors. A low score lacks discussion of intersectoral collaboration.
Key Sections to Review: Sectoral and Institutional Context, Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, Implementation Support Plan
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Core Issues to Consider: This question assesses whether the project ensures alignment and coordination across multiple stakeholders, including government agencies, development organizations, humanitarian actors, and local institutions. Poor coordination can lead to inefficiencies, conflicting mandates, or duplication of efforts, undermining project effectiveness.
High vs. Low Scores: A high score reflects clear mechanisms for coordination, such as joint working groups, formal agreements, or integrated planning frameworks. A low score indicates fragmented planning, where stakeholders work in silos without effective collaboration.
Key Sections to Review: Institutional and Implementation Arrangements, Project Components, Key Risks and Mitigation Measures, Results Framework and Monitoring
Analysis: [Your analysis here]
Probabilities: [probabilities for each score]
Log Probabilites: [log probabilities for each score]
Score: [0-10]
Running sum: [Sum of scores for questions till now]

Overall FCV Sensitivity Score
Total Score: [Sum of scores for all questions]
Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]

"""

PROMPT_4_PROBS =  """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Scoring System:
3 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.
2 = Moderately Addressed: The PAD adequately addresses the question but may lack depth or completeness.
1 = Weakly Addressed: The PAD references the issue but in a limited, superficial, or indirect way.
0 = Not Addressed: There is no evidence in the PAD that the issue has been addressed.

Output Format:
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: (give an array of probabilities for all possible scores with their corresponding scores like below)
(Ensure that the sum of probabilities across all possible scores for each question is always equal to 1)
score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

At the end, provide:
Summary: [Brief summary of the PAD's FCV sensitivity]

Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]

Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]


Overall Summary: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]
"""

PROMPT_NEW = """You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Output Format: [give the output only in the format below]
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
(give an array of probabilities for all possible scores with their corresponding scores like below)
(Ensure that the sum of probabilities across all possible scores for each question is always equal to 1)

At the end, provide:
Summary: [Brief summary of the PAD's FCV sensitivity]

Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
Revised Guiding Question: Does the PAD recognize FCV as a key risk in both the background and key risks sections, and does it identify specific pathways through which climate impacts (e.g., floods, droughts, storms) interact with FCV dynamics (e.g., resource scarcity, governance challenges, social tensions)?
Core Issues to Consider:
At a minimum, the PAD should meaningfully mention FCV-related risks within its background and key risks sections, indicating that FCV is a potential barrier to project implementation. The document should not only acknowledge these risks but also offer some explanation—even if basic—of the causal pathways (for example, how climate-induced resource scarcity might lead to governance challenges or social tensions).
Scoring Details:
Score 0: The PAD does not provide any meaningful mention of FCV-related risks in the background or key risks sections.
Score 1: The PAD makes a minimal or vague reference to FCV-related risks but does not explain how climate impacts might trigger or worsen these dynamics.
Score 2: The PAD meaningfully mentions FCV-related risks and offers a basic explanation of potential impacts; however, the description of causal pathways is generic and lacks in-depth context.
Score 3: The PAD offers a comprehensive analysis by meaningfully mentioning FCV-related risks and clearly explaining specific causal pathways with context-specific examples (e.g., detailing how climate-induced resource scarcity leads to governance challenges or social tensions).
Key Sections to Review:
Background/Context and Key Risks and Implementation Arrangements
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0-3]
Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
This characteristic is divided into two sub-questions.
2A. Preventing Maladaptation in Project Interventions
Revised Guiding Question 2A: Does the PAD describe specific measures or actions that ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Core Issues to Consider:
At a minimum, the PAD should indicate that measures or actions exist to prevent project interventions from heightening FCV-related risks. It should demonstrate awareness that its activities might unintentionally intensify vulnerabilities. Higher scores are awarded when the PAD clearly articulates well-defined, context-specific measures or actions—detailing how the project will monitor its impacts and adjust interventions to minimize negative outcomes and respond to emerging FCV-related tensions.
Scoring Details:
Score 0: The PAD does not provide any meaningful mention of measures or actions to prevent the exacerbation of FCV-related vulnerabilities.
Score 1: The PAD makes a minimal or vague reference to the need for such measures, without describing specific actions to mitigate FCV vulnerabilities.
Score 2: The PAD meaningfully mentions that measures or actions will be taken to prevent worsening FCV-related vulnerabilities, although the description is basic and lacks detailed explanation.
Score 3: The PAD offers a comprehensive strategy by clearly describing specific, context-specific measures or actions. It explains how the project will continuously monitor its impacts and adjust interventions to prevent exacerbation of FCV-related vulnerabilities, providing thorough examples and mechanisms.
Key Sections to Review:
Key Risks and Mitigation Measures, Implementation Arrangements, Social Safeguards, and sections detailing project design or monitoring mechanisms.
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0-3]
2B. Adaptive Project Design
Revised Guiding Question 2B: To what extent does the PAD incorporate adaptive mechanisms in project design that balance short-term needs with long-term resilience building in an FCV setting and account for various scenarios of FCV evolution and potential escalation?
Core Issues to Consider:
At a minimum, the PAD should acknowledge the need to balance immediate interventions with long-term resilience in FCV settings and indicate some awareness of potential shifts in the FCV context. Higher scores are given when the PAD outlines clear adaptive mechanisms—such as detailed scenario planning or specific contingency measures—that enable the project to adjust to different FCV scenarios and escalation risks.
Scoring Details:
Score 0: The PAD does not mention any adaptive mechanisms or evidence of balancing short-term needs with long-term resilience.
Score 1: The PAD makes a minimal reference to adaptive project design without specifying how it will address varied FCV scenarios or long-term resilience.
Score 2: The PAD acknowledges the need for adaptive measures and balance between short-term and long-term needs; however, the measures described are generic and lack sufficient detail or examples.
Score 3: The PAD provides a comprehensive strategy that incorporates detailed, tailored adaptive mechanisms. It clearly demonstrates how short-term interventions are balanced with long-term resilience objectives, supported by specific examples and thorough scenario-based planning.
Key Sections to Review:
Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, and Sustainability/Long-Term Planning
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0-3]
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
Revised Guiding Question: Does the PAD include interventions that explicitly address the root causes of FCV (such as inequitable access to resources or weak governance) and seek to promote activities related to peacebuilding (directly or indirectly) where relevant?
Core Issues to Consider:
At a minimum, the PAD should identify and address the root causes of FCV by highlighting issues such as governance deficits or resource inequities. The document should at least outline these challenges in basic terms. Higher scores are given when the PAD additionally identifies opportunities to promote activities related to peacebuilding—such as fostering dialogue, trust, or social cohesion—where relevant to the context of the intervention.
Scoring Details:
Score 0: The PAD does not identify or address the root causes of FCV.
Score 1: The PAD offers a minimal or superficial mention of FCV root causes without including any activities related to peacebuilding.
Score 2: The PAD identifies the root causes of FCV (for example, governance deficits or resource inequities) and hints at the potential for related peacebuilding activities, but without describing concrete actions.
Score 3: The PAD provides a comprehensive strategy that explicitly addresses both the root causes of FCV and, where relevant, seeks to promote peacebuilding activities. It includes detailed, context-specific analysis that demonstrates an effort to incorporate opportunities for fostering dialogue, trust, or social cohesion.
Key Sections to Review:
Country Context, Sectoral and Institutional Context, and Project Components
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0-3]
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
Revised Guiding Question: Does the PAD identify vulnerable populations at risk of FCV (such as women, displaced persons, and minorities) and actively propose measures to address inequalities through targeted interventions and equitable benefit sharing?
Core Issues to Consider:
At a minimum, the PAD should clearly identify vulnerable groups and meaningfully discuss their specific FCV-related needs, rather than providing only cursory mentions. Higher scores are awarded when the PAD not only identifies these groups but also outlines concrete, targeted strategies—such as social impact assessments or grievance redress mechanisms—that promote equitable benefit sharing and actively address existing inequalities.
Scoring Details:
Score 0: The PAD does not meaningfully identify vulnerable populations or discuss their FCV-related needs.
Score 1: The PAD offers only minimal or vague references to vulnerable populations without providing specific details on their needs or targeted interventions.
Score 2: The PAD clearly identifies vulnerable groups and outlines their needs; however, the measures proposed to address inequalities or ensure equitable benefit sharing are basic and lack depth.
Score 3: The PAD provides a comprehensive and in-depth strategy that not only identifies vulnerable populations and their needs but also articulates robust, targeted interventions to ensure equitable benefit sharing and effectively address systemic inequalities related to FCV.
Key Sections to Review:
Country Context, Social Sections (including Safeguards), Project Beneficiaries, and Results Framework and Monitoring
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0-3]
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
Revised Guiding Question: Does the PAD engage with a diverse range of stakeholders (especially beyond government) and outline mechanisms to prevent mandate duplication while ensuring active coordination among humanitarian, peacebuilding, and disaster risk management actors?
Core Issues to Consider:
At a minimum, the PAD should provide meaningful evidence of stakeholder engagement—this could include references to consultations or participation in relevant networks. Higher scores are reserved for PADs that detail formal coordination mechanisms (for example, through joint working groups or integrated planning frameworks) that actively prevent mandate duplication and foster robust cross-sector collaboration.
Scoring Details:
Score 0: The PAD does not provide any meaningful evidence of stakeholder engagement.
Score 1: The PAD offers only minimal references to stakeholder engagement, with no detailed coordination mechanisms presented.
Score 2: The PAD demonstrates basic stakeholder engagement and mentions some coordination mechanisms; however, the description is generic and lacks specificity.
Score 3: The PAD provides a comprehensive and detailed account of stakeholder engagement and formal coordination mechanisms. It clearly outlines structures and processes that prevent mandate duplication and foster active, cross-sector collaboration among humanitarian, peacebuilding, and DRM actors.
Key Sections to Review:
Sectoral and Institutional Context, Institutional and Implementation Arrangements, Key Risks and Mitigation Measures, Social Safeguards, and Implementation Support Plan
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0-3]
Overall FCV Sensitivity Score
Total Score: [Sum of scores for all characteristics and sub-questions, as applicable]
Summary:
Provide a brief reflection on the PAD’s overall strengths and weaknesses in incorporating FCV-sensitive measures. Your summary should highlight how well the document integrates risk identification, adaptive project design (both preventive measures and adaptive mechanisms), addressing root causes with opportunities for peacebuilding, protection of vulnerable groups, and cross-sector coordination—while also noting areas for improvement.
"""

PROMPT_NEW_VERSION2 = """
You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0–3) for each question and provide a detailed analysis to justify your score.
 
⚠️ Note: In previous applications of this protocol, the model has produced more pessimistic scoring outcomes (especially for score levels 0 and 1) than manual expert reviews. To improve consistency, we have **softened the interpretation of scores 0 and 1**. Please consider partial, implicit, or general references as partial evidence, and use the revised definitions below. Be generous where minimal acknowledgment exists, even if details are sparse.
 
###############################
# Softened Scoring Definitions
###############################
 

Score 0: The PAD does not clearly articulate or provide a meaningful mention of the issue. Any reference is either too implicit, peripheral, or not relevant enough to FCV.
Score 1: The PAD acknowledges the issue at a basic level, but the reference is vague, generic, or only indirectly stated. It reflects awareness but lacks elaboration or clear action.
Score 2: The PAD meaningfully references the issue and includes some explanation or intent, though it may be somewhat general or underdeveloped.
Score 3: The PAD provides a clear, detailed, and context-specific discussion of the issue, with concrete actions, mechanisms, or examples.
 
Now assess the PAD using the following:

 
###############################
# Output Format
###############################
 
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
(Ensure the sum of all four probabilities equals 1)
Score: [0–3]
 
At the end, provide:
Summary: [Brief summary of the PAD’s FCV sensitivity]
 
###############################
# Begin FCV Protocol
###############################
 
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
Revised Guiding Question: Does the PAD recognize FCV as a key risk in both the background and key risks sections, and does it identify specific pathways through which climate impacts (e.g., floods, droughts, storms) interact with FCV dynamics (e.g., resource scarcity, governance challenges, social tensions)?
Core Issues to Consider:
At a minimum, the PAD should meaningfully mention FCV-related risks within its background and key risks sections, indicating that FCV is a potential barrier to project implementation. The document should not only acknowledge these risks but also offer some explanation—even if basic—of the causal pathways (e.g., how climate-induced resource scarcity might lead to governance challenges or social tensions).
Scoring Details:
Score 0: The PAD does not clearly articulate or provide a meaningful mention of FCV-related risks. Any reference is too implicit or disconnected.
Score 1: The PAD acknowledges FCV-related risks at a basic level, but does not explain how climate impacts might trigger or worsen these dynamics.
Score 2: The PAD meaningfully mentions FCV-related risks and offers a basic explanation of potential impacts; however, the description of causal pathways is generic.
Score 3: The PAD offers a comprehensive analysis by clearly explaining specific causal pathways with context-specific examples.
 
Key Sections to Review:
Background/Context and Key Risks and Implementation Arrangements
 
Analysis: [Your analysis here]
Probabilities: score 0 [ ], score 1 [ ], score 2 [ ], score 3 [ ]
Score: [0–3]
 
Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
This characteristic is divided into two sub-questions.
 
2A. Preventing Maladaptation in Project Interventions  
Revised Guiding Question 2A: Does the PAD describe specific measures or actions that ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
Scoring Details:
Score 0: The PAD does not clearly indicate any measures to prevent exacerbation of FCV-related vulnerabilities.
Score 1: The PAD includes a basic or vague acknowledgment of this need, but does not specify mitigation measures.
Score 2: The PAD mentions meaningful but basic measures, lacking detail.
Score 3: The PAD provides a comprehensive strategy including clear, context-specific actions with monitoring and mitigation mechanisms.
 
Key Sections to Review:
Key Risks and Mitigation Measures, Implementation Arrangements, Social Safeguards
 
Analysis: [Your analysis here]
Probabilities: score 0 [ ], score 1 [ ], score 2 [ ], score 3 [ ]
Score: [0–3]
 
2B. Adaptive Project Design  
Revised Guiding Question 2B: To what extent does the PAD incorporate adaptive mechanisms in project design that balance short-term needs with long-term resilience in an FCV setting?
Scoring Details:
Score 0: No mention of adaptive mechanisms or planning for FCV context shifts.
Score 1: Basic or general acknowledgment of the need for adaptation, but no detail on how it would be implemented.
Score 2: PAD recognizes the need and outlines general mechanisms, but lacks specificity.
Score 3: Provides detailed, scenario-based planning with clear adaptive measures.
 
Key Sections to Review:
Implementation Arrangements, Key Risks and Mitigation Measures, Sustainability
 
Analysis: [Your analysis here]
Probabilities: score 0 [ ], score 1 [ ], score 2 [ ], score 3 [ ]
Score: [0–3]
 
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding  
Revised Guiding Question: Does the PAD include interventions that address FCV root causes and support peacebuilding activities?
 
Scoring Details:
Score 0: Does not identify or address root causes of FCV.
Score 1: Minimally acknowledges FCV issues, but no peacebuilding interventions are described.
Score 2: Identifies root causes and hints at peacebuilding potential, but actions are not concrete.
Score 3: Clearly addresses root causes and includes specific, relevant peacebuilding actions.
 
Key Sections to Review:
Country Context, Institutional Context, Project Components
 
Analysis: [Your analysis here]
Probabilities: score 0 [ ], score 1 [ ], score 2 [ ], score 3 [ ]
Score: [0–3]
 
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups  
Revised Guiding Question: Does the PAD identify vulnerable populations and propose targeted interventions to address inequalities?
 
Scoring Details:
Score 0: Does not meaningfully identify vulnerable groups or their needs.
Score 1: General or superficial mention of vulnerable populations, with no clear actions.
Score 2: Identifies specific groups and outlines general responses.
Score 3: Offers detailed, robust, and equity-focused interventions with mechanisms.
 
Key Sections to Review:
Country Context, Social Sections, Project Beneficiaries, Monitoring
 
Analysis: [Your analysis here]
Probabilities: score 0 [ ], score 1 [ ], score 2 [ ], score 3 [ ]
Score: [0–3]
 
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors  
Revised Guiding Question: Does the PAD engage a diverse range of actors and outline coordination mechanisms to avoid duplication?
 
Scoring Details:
Score 0: No meaningful evidence of stakeholder engagement or coordination.
Score 1: Vague references to engagement, no structure provided.
Score 2: Mentions coordination, but mechanisms are basic.
Score 3: Describes formal, structured coordination and cross-sector collaboration.
 
Key Sections to Review:
Institutional Context, Implementation Arrangements, Risks, Social Safeguards
 
Analysis: [Your analysis here]
Probabilities: score 0 [ ], score 1 [ ], score 2 [ ], score 3 [ ]
Score: [0–3]
 
###############################
Overall FCV Sensitivity Score
###############################
 
Total Score: [Sum of all scores]
Summary: [Brief reflection on strengths and gaps in FCV sensitivity across the five characteristics.]
"""

PROMPT_NEW_VERSION3 = """ You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.

Output Format: [give the output only in the format below]
For each characteristic, provide the following:
Guiding Question: [Question]
Analysis: [Detailed analysis of how the PAD addresses the question]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
(give an array of probabilities for all possible scores with their corresponding scores like below)
(Ensure that the sum of probabilities across all possible scores for each question is always equal to 1)

At the end, provide:
Summary: [Brief summary of the PAD's FCV sensitivity]

Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
Revised Guiding Question:
Does the PAD recognize FCV as a key risk in both the background and key risks sections, and identify specific pathways through which climate impacts (e.g., floods, droughts, storms) interact with FCV dynamics (e.g., resource scarcity, governance challenges, social tensions)?
Core Issues to Consider:
The PAD should acknowledge FCV‑related risks in its background and key risks sections, indicating that FCV may impede project delivery. Higher scores require clear, context‑specific descriptions of how particular climate events translate into FCV pressures.
Scoring Details:
Score 0: The PAD does not meaningfully mention FCV‑related risks in background or key risks sections.
Score 1: The PAD acknowledges FCV‑related risks as part of the background and key risks sections; references to FCV-related risks may be brief or indirect.
Score 2: The PAD meaningfully mentions FCV‑related risks and provides a basic explanation of potential impacts; however, the description of causal pathways remains generic.
Score 3: The PAD provides a detailed, context‑specific analysis linking climate impacts to FCV dynamics, with clear examples and mechanisms.
Key Sections to Review:
Background/Context; Key Risks and Implementation Arrangements
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0–3]

Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

2A. Preventing Maladaptation in Project Interventions
Revised Guiding Question 2A:
Does the PAD describe measures or actions that ensure project interventions do not exacerbate FCV‑related vulnerabilities or create new sources of tension?
Core Issues to Consider:
The PAD should indicate that it has considered measures to prevent harm to FCV‑sensitive groups. Higher scores require clear, context‑specific actions, including plans for monitoring and adjustment.
Scoring Details:
Score 0: The PAD does not mention any measures or actions to prevent exacerbation of FCV‑related vulnerabilities.
Score 1: The PAD acknowledges the need to avoid exacerbating FCV vulnerabilities in relevant sections; references may be conceptual or implied.
Score 2: The PAD describes specific measures or actions in general terms, though lacking robust detail.
Score 3: The PAD outlines a comprehensive, context‑specific set of measures or actions, including mechanisms for monitoring and iterative adjustment.
Key Sections to Review:
Key Risks and Mitigation Measures; Implementation Arrangements; Social Safeguards
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0–3]

2B. Adaptive Project Design
Revised Guiding Question 2B:
To what extent does the PAD incorporate adaptive mechanisms that balance short‑term needs with long‑term resilience in an FCV setting?
Core Issues to Consider:
The PAD should show awareness that FCV conditions can evolve. Higher scores require detailed, scenario‑based or contingency plans specifying how the project will adjust under different FCV scenarios.
Scoring Details:
Score 0: The PAD does not refer to adaptive mechanisms or planning for evolving FCV contexts.
Score 1: The PAD acknowledges the need for adaptation in relevant sections; references may be conceptual or implied.
Score 2: The PAD outlines general adaptive mechanisms without detailed implementation plans.
Score 3: The PAD presents detailed, scenario‑based planning with clear triggers and adaptive measures.
Key Sections to Review:
Implementation Arrangements; Key Risks and Mitigation Measures; Sustainability/Long‑Term Planning
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0–3]

Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
Revised Guiding Question:
Does the PAD include interventions that explicitly address the root causes of FCV (e.g., inequitable resource access, weak governance) and seek to promote peacebuilding activities (directly or indirectly) where relevant?
Core Issues to Consider:
The PAD should identify FCV root causes in the Country and Institutional Context. Higher scores require, where relevant, concrete steps to foster dialogue, trust, or social cohesion alongside climate interventions.
Scoring Details:
Score 0: The PAD does not identify or address the root causes of FCV.
Score 1: The PAD acknowledges FCV root causes in relevant sections; references to peacebuilding may be indirect or conceptual.
Score 2: The PAD identifies root causes and suggests potential peacebuilding opportunities, but without concrete actions.
Score 3: The PAD integrates clear interventions addressing root causes and, where relevant, includes specific peacebuilding activities with contextual examples.
Key Sections to Review:
Country Context; Sectoral and Institutional Context; Project Components
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0–3]

Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
Revised Guiding Question:
Does the PAD identify vulnerable populations at risk of FCV (e.g., women, displaced persons, minorities) and propose targeted interventions to address inequalities and ensure equitable benefit sharing?
Core Issues to Consider:
The PAD should meaningfully identify vulnerable groups and their FCV‑related needs. Higher scores require robust, targeted strategies—such as social impact assessments or grievance mechanisms—to actively redress inequalities.
Scoring Details:
Score 0: The PAD does not identify vulnerable populations or discuss their FCV‑related needs.
Score 1: The PAD acknowledges vulnerable populations and their needs in relevant sections; references may be general or implied.
Score 2: The PAD identifies specific groups and outlines general interventions, though lacking detailed mechanisms.
Score 3: The PAD details robust, equity‑focused interventions with clear mechanisms ensuring benefits reach vulnerable groups.
Key Sections to Review:
Country Context; Social Sections (including Safeguards); Project Beneficiaries; Results Framework and Monitoring
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0–3]

Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
Revised Guiding Question:
Does the PAD engage a diverse range of actors (especially beyond government) and outline coordination mechanisms to prevent mandate duplication and foster cross‑sector collaboration?
Core Issues to Consider:
The PAD should provide evidence of stakeholder engagement. Higher scores require formal structures—such as joint working groups or integrated frameworks—that actively coordinate across sectors.
Scoring Details:
Score 0: The PAD does not provide meaningful evidence of stakeholder engagement or coordination mechanisms.
Score 1: The PAD acknowledges the importance of stakeholder engagement in relevant sections; references may be general or implied.
Score 2: The PAD mentions coordination and describes basic mechanisms, though without a fully structured approach.
Score 3: The PAD outlines well‑defined, formal coordination mechanisms and demonstrates active, cross‑sector collaboration.
Key Sections to Review:
Sectoral and Institutional Context; Institutional and Implementation Arrangements; Key Risks and Mitigation Measures; Social Safeguards; Implementation Support Plan
Analysis: [Your analysis here]
Probabilities: score 0 [probability], score 1 [probability], score 2 [probability], score 3 [probability]
Score: [0–3]

Overall FCV Sensitivity Score
Total Score: Sum of the five characteristic scores (each 0–3).
Summary: A concise reflection on the PAD’s overall FCV sensitivity, noting where the PAD demonstrates basic acknowledgment (Score 1), meaningful engagement (Score 2), and in‑depth treatment (Score 3), as well as any gaps needing attention."""

ALL_PROMPTS = {
    # "Prompt 1": PROMPT_1,
    # "Prompt 2": PROMPT_2,
    # "Prompt 3": PROMPT_3,
    # "Prompt 4": PROMPT_4,
    # "Prompt 5": PROMPT_5,
    # "Prompt 2 (part 1)": PROMPT_2_LOGG_1,
    # "Prompt 2 (part 2)": PROMPT_2_LOGG_2,
    # "Prompt 4 (Important sections)": PROMPT_4_IMP,
    # "Prompt 2 (Important sections)": PROMPT_2_IMP,
    "Prompt 4 (Log probability)": PROMPT_4_LOG,
    "Prompt 2 (Log probability)": PROMPT_2_LOG,
    "Prompt 4 (Important sections with logprobability)": PROMPT_4_IMP_LOG,
    "Prompt 2 (Important sections with logprobability)": PROMPT_2_IMP_LOG,
    "Prompt 4 (Probabilities)": PROMPT_4_PROBS,
    "Prompt new": PROMPT_NEW,
    "PROMPT NEW Version2": PROMPT_NEW_VERSION2,
    "PROMPT NEW Version3": PROMPT_NEW_VERSION3,
    
}
