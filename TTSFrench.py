# Code to use Google text to speech

from google.cloud import texttospeech
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="text-to-speech-key.json"

project_id = ENV['PROJECT_ID']
location = 'global'
output_gcs_uri = 'gs://alohadoo-posts/bipolarity-research.wav'

def synthesize_long_audio(project_id, location, output_gcs_uri):

    client = texttospeech.TextToSpeechLongAudioSynthesizeClient()

    input = texttospeech.SynthesisInput(
        text="""L'état de la recherche sur le trouble bipolaire
                Le trouble bipolaire, anciennement appelé maniaco-dépression, est une maladie mentale qui se caractérise par des alternances de phases d'excitation (maniaques ou hypomaniaques) et de phases de dépression. Ces fluctuations de l'humeur ont un impact majeur sur la qualité de vie, la santé et le fonctionnement social des personnes atteintes. Selon les estimations, environ 1% de la population mondiale souffre de trouble bipolaire, qui est l'une des six causes principales de handicap.
                Malgré la gravité de cette pathologie, les causes et les mécanismes du trouble bipolaire restent en grande partie méconnus. La recherche sur ce sujet accuse un certain retard par rapport à d'autres maladies mentales, comme la schizophrénie ou la dépression. Toutefois, ces dernières années, des progrès significatifs ont été réalisés grâce à des approches multidisciplinaires et à des cohortes de patients suivis sur le long terme.
                Les facteurs génétiques et environnementaux
                Le trouble bipolaire est une maladie multifactorielle, c'est-à-dire qu'elle résulte de l'interaction entre des facteurs génétiques et des facteurs environnementaux. Les études familiales et jumelles ont montré que le risque de développer un trouble bipolaire est plus élevé chez les personnes ayant un parent du premier degré atteint. Toutefois, il n'existe pas un seul gène responsable du trouble bipolaire, mais plutôt plusieurs variants génétiques qui augmentent la vulnérabilité à la maladie.
                Parmi ces variants, certains concernent le système immunitaire, notamment les gènes HLA (Human Leukocyte Antigen) et TLR (Toll-like Receptor), qui sont impliqués dans la reconnaissance et la réponse aux agents infectieux. Ces gènes rendent les personnes porteuses plus sensibles à des facteurs de risque environnementaux, comme les infections, les traumatismes, la pollution ou le stress. Ces facteurs peuvent déclencher ou aggraver une inflammation chronique, qui perturbe le fonctionnement du cerveau et des neurotransmetteurs, comme la sérotonine ou la dopamine.
                Les trajectoires et les comorbidités
                Le trouble bipolaire est une maladie évolutive, qui ne se limite pas à un seul épisode. La plupart des patients présentent des rechutes et des rémissions tout au long de leur vie, avec des conséquences néfastes sur leur santé physique et mentale. Le trouble bipolaire est associé à une réduction de l'espérance de vie de 10 ans, en raison du risque élevé de suicide, mais aussi de comorbidités somatiques, comme les maladies cardiovasculaires, le diabète ou l'obésité.
                Pour mieux comprendre les trajectoires du trouble bipolaire, la fondation FondaMental a créé en 2010 la cohorte FACE-BD (FondaMental Advanced Center of Expertise for Bipolar Disorder), qui regroupe plus de 4 000 patients suivis régulièrement par des centres experts. Cette cohorte a permis de mettre en évidence des facteurs de mauvais pronostic, comme les traumatismes infantiles, les troubles du sommeil, les addictions ou les troubles anxieux. Elle a également permis de décrire les différentes formes cliniques du trouble bipolaire, qui varient selon la fréquence, la durée et la sévérité des épisodes, ainsi que selon la présence ou non de symptômes psychotiques.
                Les traitements et les stratégies thérapeutiques
                Le traitement du trouble bipolaire repose principalement sur les médicaments stabilisateurs de l'humeur, comme le lithium, le valproate ou la lamotrigine, qui visent à prévenir les rechutes et à réduire la sévérité des épisodes. Ces médicaments sont souvent associés à des antidépresseurs, des antipsychotiques ou des anxiolytiques, selon les besoins de chaque patient. Toutefois, ces traitements ne sont pas efficaces chez tous les patients, et peuvent avoir des effets secondaires indésirables.
                La recherche sur les traitements du trouble bipolaire s'oriente vers deux axes principaux : d'une part, l'identification de biomarqueurs qui permettraient de prédire la réponse aux médicaments et d'adapter la posologie ; d'autre part, le développement de nouvelles molécules ciblant les voies biologiques impliquées dans la maladie, comme l'inflammation ou le stress oxydatif.
                Par ailleurs, les traitements médicamenteux doivent être complétés par des interventions psychosociales, qui visent à améliorer la qualité de vie, l'adhésion au traitement, la gestion du stress et la prévention des rechutes. Parmi ces interventions, on peut citer la psychoéducation, qui consiste à informer le patient et son entourage sur la maladie et ses traitements ; la thérapie cognitivo-comportementale, qui vise à modifier les pensées et les comportements négatifs ; la remédiation cognitive, qui propose des exercices pour améliorer les fonctions cognitives altérées, comme la mémoire ou l'attention ; ou encore les outils numériques, qui offrent un suivi à distance et une alerte en cas de dégradation de l'état du patient.
                Le trouble bipolaire est une maladie complexe et hétérogène, qui nécessite une prise en charge personnalisée et multidimensionnelle. La recherche sur ce sujet a permis de faire des avancées importantes dans la compréhension des causes, des mécanismes, des trajectoires et des traitements du trouble bipolaire. Toutefois, il reste encore de nombreux défis à relever, comme le dépistage précoce, la prévention des complications, l'amélioration de l'efficacité et de la tolérance des médicaments, ou encore le développement de nouvelles approches thérapeutiques innovantes."""
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000
    )

    voice = texttospeech.VoiceSelectionParams(
        language_code="fr-FR", name="fr-FR-Polyglot-1"
    )

    parent = f"projects/{project_id}/locations/{location}"

    request = texttospeech.SynthesizeLongAudioRequest(
        parent=parent,
        input=input,
        audio_config=audio_config,
        voice=voice,
        output_gcs_uri=output_gcs_uri,
    )

    operation = client.synthesize_long_audio(request=request)
    # Set a deadline for your LRO to finish. 300 seconds is reasonable, but can be adjusted depending on the length of the input.
    # If the operation times out, that likely means there was an error. In that case, inspect the error, and try again.
    result = operation.result(timeout=300)
    print(
        "\nFinished processing, check your GCS bucket to find your audio file! Printing what should be an empty result: ",
        result,
    )

synthesize_long_audio(project_id, location, output_gcs_uri)
