import re
import json


test_llm_output = """"" \
### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery

#### Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
**Analysis:** The PAD acknowledges potential risks related to institutional weaknesses in local agencies and highlights the fragmented nature of service delivery, which can create barriers to effective implementation. However, while it mentions capacity risks and the need for inter-agency coordination, it does not directly address specific security risks or community relations issues that could affect project delivery.
**Probabilities:** score 0 [10%], score 1 [30%], score 2 [40%], score 3 [20%]  
**Log Probabilities:** score 0 [-2.3], score 1 [-1.2], score 2 [-0.4], score 3 [-1.6]  
**Score:** 2  
**Running sum:** 2  

#### Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
**Analysis:** The PAD does discuss climate-related impacts, especially regarding flooding and water supply issues exacerbated by climate change. However, it does not sufficiently detail the interactions of these climate impacts with FCV dynamics, such as how they may influence community tensions or resource access conflicts. This limits the thoroughness of the assessment.
**Probabilities:** score 0 [15%], score 1 [40%], score 2 [30%], score 3 [15%]  
**Log Probabilities:** score 0 [-1.9], score 1 [-0.4], score 2 [-0.5], score 3 [-1.9]  
**Score:** 1  
**Running sum:** 3  

### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation

#### Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
**Analysis:** The PAD outlines the Social Management Framework (SMF) that aims to address involuntary resettlement and ensure that affected persons’ livelihoods are restored. While this is a positive measure, the specifics on how interventions will directly avoid exacerbating FCV-related vulnerabilities are limited, leading to uncertainties in effectiveness.
**Probabilities:** score 0 [20%], score 1 [40%], score 2 [30%], score 3 [10%]  
**Log Probabilities:** score 0 [-1.6], score 1 [-0.4], score 2 [-0.5], score 3 [-2]  
**Score:** 1  
**Running sum:** 4  

#### Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
**Analysis:** The PAD suggests the establishment of a Project Management Unit (PMU) with necessary staff. However, it lacks explicit mechanisms for adapting to changing FCV conditions over the project’s life cycle. The reference to technical assistance and capacity-building measures is positive but insufficiently detailed to score higher.
**Probabilities:** score 0 [25%], score 1 [30%], score 2 [35%], score 3 [10%]  
**Log Probabilities:** score 0 [-1.4], score 1 [-0.4], score 2 [-0.4], score 3 [-2]  
**Score:** 1  
**Running sum:** 5  

#### Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
**Analysis:** The PAD discusses immediate urban service improvements and infrastructure upgrades but does not adequately demonstrate how these will lead to long-term resilience or avoid maladaptive outcomes. The absence of a clear resilience strategy limits the depth of this aspect.
**Probabilities:** score 0 [30%], score 1 [45%], score 2 [20%], score 3 [5%]  
**Log Probabilities:** score 0 [-1.2], score 1 [-0.2], score 2 [-0.7], score 3 [-2.3]  
**Score:** 1  
**Running sum:** 6  

### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding

#### Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
**Analysis:** The PAD acknowledges issues such as inadequate urban services and governance fragmentation but does not explicitly connect these to root causes of FCV, such as inequitable resource access or governance failures. There is a lack of targeted interventions addressing these deeper issues.
**Probabilities:** score 0 [40%], score 1 [35%], score 2 [20%], score 3 [5%]  
**Log Probabilities:** score 0 [-0.4], score 1 [-0.2], score 2 [-0.7], score 3 [-2.3]  
**Score:** 1  
**Running sum:** 7  

#### Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
**Analysis:** The PAD mentions community engagement through consultative committees and the establishment of a grievance redress mechanism but lacks a comprehensive strategy for promoting peacebuilding or social cohesion explicitly connected to the project interventions.
**Probabilities:** score 0 [30%], score 1 [40%], score 2 [25%], score 3 [5%]  
**Log Probabilities:** score 0 [-1.2], score 1 [-0.4], score 2 [-0.6], score 3 [-2.3]  
**Score:** 1  
**Running sum:** 8  

### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups

#### Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
**Analysis:** The PAD includes a gender action plan as part of the Social Management Framework, indicating some recognition of vulnerable groups' needs. However, the identification of other specific vulnerable populations remains limited, and the measures proposed lack depth and comprehensiveness.
**Probabilities:** score 0 [20%], score 1 [35%], score 2 [35%], score 3 [10%]  
**Log Probabilities:** score 0 [-1.6], score 1 [-0.4], score 2 [-0.4], score 3 [-2.0]  
**Score:** 1  
**Running sum:** 9  

#### Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
**Analysis:** The PAD does not provide sufficient detail on mechanisms for equitable benefit-sharing. While it mentions consultations and grievance redress, it lacks specific strategies to prevent reinforcing existing inequalities among different community groups.
**Probabilities:** score 0 [30%], score 1 [40%], score 2 [20%], score 3 [10%]  
**Log Probabilities:** score 0 [-1.2], score 1 [-0.4], score 2 [-0.7], score 3 [-2.3]  
**Score:** 1  
**Running sum:** 10  

### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors

#### Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
**Analysis:** The PAD outlines a multi-agency approach and the establishment of a Steering Committee for coordination. While this indicates some level of collaboration, the depth and specifics of engaging with humanitarian and peacebuilding sectors are not clearly articulated.
**Probabilities:** score 0 [20%], score 1 [30%], score 2 [30%], score 3 [20%]  
**Log Probabilities:** score 0 [-1.6], score 1 [-0.4], score 2 [-0.4], score 3 [-1.6]  
**Score:** 2  
**Running sum:** 12  

#### Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
**Analysis:** The establishment of the PMU and Steering Committee suggests mechanisms for alignment and coordination. However, the PAD does not provide extensive details on how mandate overlaps will be resolved or duplication avoided, leading to a lower score.
**Probabilities:** score 0 [25%], score 1 [35%], score 2 [30%], score 3 [10%]  
**Log Probabilities:** score 0 [-1.4], score 1 [-0.4], score 2 [-0.5], score 3 [-2.3]  
**Score:** 1  
**Running sum:** 13  

### Overall FCV Sensitivity Score
**Total Score:** 13  
**Summary:** The PAD addresses several aspects of FCV sensitivity, including recognition of climate impacts and some consideration for vulnerable populations. However, overall, the document lacks depth in connecting these aspects to systemic barriers related to FCV, such as governance issues and security risks. The mechanisms for addressing these issues are underdeveloped, leading to a moderate overall FCV sensitivity score. There is room for improvement in explicitly linking climate actions to peace" \

"""


def extract_score_probabilities_and_scores(llm_output: str):
    output = {}
    total_score = 0
    characteristic = None
    question_index = 0

    lines = llm_output.split('\n')
    for line in lines:
        # Match characteristic headers
        char_match = re.match(r'^### Characteristic \d+: (.+)', line)
        if char_match:
            characteristic = char_match.group(1).strip()
            output[characteristic] = []
            question_index = 0
            continue
        
        # Match guiding question
        question_match = re.match(r'^#### Guiding Question: (.+)', line)
        if question_match and characteristic:
            question = question_match.group(1).strip()
            output[characteristic].append({
                'question': question,
                'probabilities': {},
                'score': None
            })
            continue
        
        # Match probabilities line
        prob_match = re.match(r'^\*\*Probabilities:\*\* score 0 \[(\d+)%\], score 1 \[(\d+)%\], score 2 \[(\d+)%\], score 3 \[(\d+)%\]', line)
        if prob_match and characteristic:
            probs = list(map(int, prob_match.groups()))
            probs_dict = {
                'score_0': probs[0],
                'score_1': probs[1],
                'score_2': probs[2],
                'score_3': probs[3],
            }

            # Get all indices (scores) with the maximum probability
            max_prob = max(probs)
            max_scores = [i for i, prob in enumerate(probs) if prob == max_prob]
            max_score = max(max_scores)  # Prefer higher score if tie

            output[characteristic][question_index]['probabilities'] = probs_dict
            output[characteristic][question_index]['score'] = max_score
            total_score += max_score
            question_index += 1

    return output, total_score



# Example usage
if __name__ == "__main__":
    scores, total_score = extract_score_probabilities_and_scores(test_llm_output)
    print(json.dumps(scores, indent=4))
    print(f"Total Score: {total_score}")