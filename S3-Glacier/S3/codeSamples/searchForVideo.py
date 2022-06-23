import copy

from spikyai_aws_libs.s3.s3 import AwsS3Client

s3_client = AwsS3Client()

"""
platform-ml-infra-data-generation
platform-ml-infra-data-preparation
platform-ml-infra-data-analysis
"""


def get_buckets(env):
    return {
        'data_generation': f'platform-ml-infra-data-generation-{env}',
        'data_prep': f'platform-ml-infra-data-preparation-{env}',
        'data_analysis': f'platform-ml-infra-data-analysis-{env}',
    }


def get_required_outputs(video_id):
    return {
        'data_generation': [
            f'sdfdg_outputs/{video_id}.json',
            f'sdvdg_artifacts/audios/{video_id}_audio.wav',
            f'sdvdg_artifacts/transcribe_outputs/{video_id}_audio_transcribe_output.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_encouragement_results.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_objectivity_results.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_offensiveness_results.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_positivity_results.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_proficiency_results.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_sarcasm_results.json',
            f'sdvsdg_outputs/speech/{video_id}_speech_emotion_results.json',
            f'sdvsdg_outputs/speech/{video_id}_speech_energy_results.json',
            f'sdvndg_outputs/nlp/{video_id}_nlp_question_results.json'
        ],
        'data_prep': [
            f'sd_correlation_outputs/{video_id}_correlation_results.csv',
            f'sd_correlation_outputs/{video_id}_insight.csv',
            f'sdfdg_outputs/{video_id}.csv',
            f'sdvdg_outputs/speech/{video_id}_speech_emotion_results.csv',
            f'sdvdg_outputs/speech/{video_id}_speech_energy_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_encouragement_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_objectivity_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_offensiveness_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_positivity_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_proficiency_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_sarcasm_results.csv',
            f'sdvndg_outputs/nlp/{video_id}_nlp_question_results.csv',
        ],
        'data_analysis': [
            f'sd_correlation_outputs/{video_id}_Correlations.json',
            f'sd_insight_outputs/{video_id}_InsightGeneration.json',
            f'sdfdg_outputs/{video_id}_AttentionTime.json',
            f'sdfdg_outputs/{video_id}_AverageAwakeness.json',
            f'sdfdg_outputs/{video_id}_AverageEmotion.json',
            f'sdfdg_outputs/{video_id}_EmotionTime.json',
            f'sdvdg_outputs/speech/{video_id}_ReactionSpeechEmotionHappy.json',
            f'sdvdg_outputs/speech/{video_id}_ReactionSpeechEmotionNeutral.json',
            f'sdvdg_outputs/speech/{video_id}_ReactionSpeechEnergyEnergetic.json',
            f'sdvdg_outputs/speech/{video_id}_ReactionSpeechEnergyMonotonic.json',
            f'sdvdg_outputs/speech/{video_id}_SpeechAverageEmotion.json',
            f'sdvdg_outputs/speech/{video_id}_SpeechAverageEnergy.json',
            f'sdvdg_outputs/speech/{video_id}_SpeechEmotionTime.json',
            f'sdvdg_outputs/speech/{video_id}_SpeechEnergyTime.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPAverageEncouragement.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPAverageObjectivity.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPAverageOffensiveness.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPAveragePositivity.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPAverageProficiency.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPAverageSarcasm.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPEncouragementTime.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPObjectivityTime.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPOffensivenessTime.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPPositivityTime.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPProficiencyTime.json',
            f'sdvndg_outputs/nlp/{video_id}_NLPSarcasmTime.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPEncouragementJoy.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPEncouragementOptimism.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPObjectivityObjective.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPObjectivitySubjective.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPOffensivenessNotOffensive.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPOffensivenessOffensive.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPPositivityNegative.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPPositivityPositive.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPProficiencyA2.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPProficiencyB2.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPSarcasmIrony.json',
            f'sdvndg_outputs/nlp/{video_id}_ReactionNLPSarcasmNonIrony.json',
            f'sdvndg_outputs/question/{video_id}_NLPAverageQuestionAsked.json',
            f'sdvndg_outputs/question/{video_id}_NLPInteractionCount.json',
            f'sdvndg_outputs/question/{video_id}_NLPInteractionTimeline.json',
            f'sdvndg_outputs/question/{video_id}_NLPInteractionTimelineIntervals.json',
            f'sdvndg_outputs/question/{video_id}_SpeechStatAnalysisTime.json',
        ]
    }


phases = ['data_generation', 'data_prep', 'data_analysis']


def analyse_video(video_id, env):
    buckets = get_buckets(env)
    required_outputs = get_required_outputs(video_id)

    for phase in phases:
        print(
            f"{'*' * 32}\nExecuting phase: {phase}\t"
            f"Bucket: {buckets[phase]}"
        )
        required_phase_files = copy.deepcopy(required_outputs[phase])
        s3_files = s3_client.search_object_keys(buckets[phase], video_id)

        for file in s3_files:
            try:
                required_phase_files.remove(file)
            except ValueError:
                print(
                    f'[ERROR] found extra file for video :{video_id}, file: {file}')

        if required_phase_files:
            print('Could not find the following files: ')
            print(required_phase_files)
        else:
            print("Found all files")


if __name__ == '__main__':
    # just type the video id in this section
    video_id = '{video_id}'
    # test, dev or prod
    env = 'test'
