# dashboard/views.py
import random
import time
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    # Session থেকে সর্বশেষ EEG রেজাল্ট চেক করা হচ্ছে
    eeg_data = request.session.get('latest_eeg_result', None)
    return render(request, 'dashboard/index.html', {'eeg_data': eeg_data})

def eeg_analyzer(request):
    return render(request, 'dashboard/eeg_test.html')

def simulate_eeg(request):
    time.sleep(1) # টেলিমেট্রি প্রসেসিং সিমুলেশন delay

    # ৩টি স্পেসিফিক চ্যালেঞ্জের বায়োমার্কার ভিত্তিক র্যান্ডম আউটকাম জেনারেটর
    outcomes = [
        {
            "status": "Peak Clearance (EVA Ready)",
            "overall_score": 98,
            "attention": 98,
            "working_memory": 99,
            "sleep_quality": 85,
            "circadian": "Optimal Sync (Alpha 8-12Hz Dominant)",
            "theta_alpha_ratio": "0.45 (Normal)",
            "stress_level": "Low Stress",
            "faa_val": "+0.18 (Normal Left/Right Asymmetry)",
            "frontal_status": "98/100 • Active (FAA Normal)",
            "parietal_status": "97/100 • Normal",
            "occipital_status": "Alpha: 12 µV (Circadian Sync)",
            "fatigue_risk": "Low",
            "decline_risk": "Very Low",
            "recommendation": "Peak Performance Clearance: Continue standard 24h cycle operations."
        },
        {
            "status": "Circadian Misalignment Detected",
            "overall_score": 62,
            "attention": 65,
            "working_memory": 70,
            "sleep_quality": 40,
            "circadian": "Phase Delay (Theta 4-8Hz Elevated)",
            "theta_alpha_ratio": "0.85 (High Sleepiness)",
            "stress_level": "Moderate Emotional Fatigue",
            "faa_val": "-0.15 (Slight Shift)",
            "frontal_status": "65/100 • Fatigue Imbalance",
            "parietal_status": "70/100 • Delayed Response",
            "occipital_status": "Theta: 8 µV (Drowsiness)",
            "fatigue_risk": "Moderate",
            "decline_risk": "Low",
            "recommendation": "30-min Bright Light Therapy (10,000 lux) and Melatonin Schedule required."
        },
        {
            "status": "Severe Isolation Stress & High Fatigue",
            "overall_score": 41,
            "attention": 45,
            "working_memory": 50,
            "sleep_quality": 20,
            "circadian": "Severe Desynchronization",
            "theta_alpha_ratio": "1.35 (Critical Elevated)",
            "stress_level": "High Isolation Stress",
            "faa_val": "-0.42 (High Frontal Asymmetry)",
            "frontal_status": "45/100 • High Stress Imbalance",
            "parietal_status": "50/100 • Impaired Sync",
            "occipital_status": "Delta/Theta Spike",
            "fatigue_risk": "High",
            "decline_risk": "Moderate",
            "recommendation": "Immediate Stand-down from EVA operations. VR Nature Immersion & Rest Protocol."
        }
    ]

    selected_result = random.choice(outcomes)
    # Session-এ সেভ করা হচ্ছে যাতে ড্যাশবোর্ড ও রিকমেন্ডেশন পেজে আপডেট দেখায়
    request.session['latest_eeg_result'] = selected_result
    return JsonResponse(selected_result)

def time_perception(request):
    return render(request, 'dashboard/time_perception.html')

def recommendations(request):
    eeg_data = request.session.get('latest_eeg_result', None)
    return render(request, 'dashboard/recommendations.html', {'eeg_data': eeg_data})