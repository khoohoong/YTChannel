#!/usr/bin/env bash
#
# Download all assets for "The Forgotten Worlds of Southeast Asia"
# Usage:  bash download_assets.sh
# Files land in ./forgotten_worlds_assets/
#
set -euo pipefail

OUT="forgotten_worlds_assets"
mkdir -p "$OUT"

BASE="https://d8j0ntlcm91z4.cloudfront.net/user_30b7CTGiTTJpfv3eHgP4QQtBJ1y"

# name|url  (name = local filename)
assets=(
  # --- Hero shots (Seedance, 1080p, 5s) ---
  "01_hero_flores_cave.mp4|$BASE/hf_20260624_140131_2891a779-7103-4472-af60-2d072f590bbf.mp4"
  "02_hero_austronesian_fleet.mp4|$BASE/hf_20260624_140133_e1be8710-2bf9-48e2-a4bb-b22f5d27dd41.mp4"
  "03_hero_naga_river.mp4|$BASE/hf_20260624_140144_84c61760-ac5e-461a-80d3-08cb0459d02c.mp4"
  "04_hero_angkor_aerial.mp4|$BASE/hf_20260624_140146_3af63dee-b91b-4713-9525-74f765aff51e.mp4"

  # --- Stills (Nano Banana Pro, 16:9) ---
  "05_still_floresiensis_bust.png|$BASE/hf_20260625_053250_66842ddd-855e-41a2-84d3-4dec0fc55078.png"
  "06_still_navigator_stars.png|$BASE/hf_20260625_053330_cfc6c069-544b-45d8-84b2-ce63b082ffa9.png"
  "07_still_naga_sculpture.png|$BASE/hf_20260625_053334_28cfa547-b75d-4ef0-b89a-eba3235d4b4a.png"
  "08_still_angkor_basrelief.png|$BASE/hf_20260625_053337_1f09bd94-e826-48f0-9b7a-e61bcded241d.png"

  # --- B-roll (Kling, 720p, 5s) ---
  "09_broll_hands_bone.mp4|$BASE/hf_20260625_053340_6e72ddfb-085a-49a5-adfd-50d875cc8f8e.mp4"
  "10_broll_canoe_prow.mp4|$BASE/hf_20260625_053342_5e3cf631-02b9-4b11-90d5-6ec530b982f6.mp4"
  "11_broll_misty_river.mp4|$BASE/hf_20260625_053345_be189de9-1c5b-4a9e-8573-ffee0db9e938.mp4"
  "12_broll_monk_corridor.mp4|$BASE/hf_20260625_053355_410a7799-ecfc-4a7c-a4f3-10c1a7672aae.mp4"

  # --- Voiceover (Arthur / ElevenLabs, 100.7s) ---
  "13_vo_arthur_narration.mp3|$BASE/hf_20260625_053729_dd298d94-1360-4548-a8ce-21769b8035a9.mp3"
)

echo "Downloading ${#assets[@]} assets into ./$OUT/ ..."
fail=0
for entry in "${assets[@]}"; do
  name="${entry%%|*}"
  url="${entry#*|}"
  printf '  -> %s\n' "$name"
  if ! curl -fSL --retry 4 --retry-delay 2 -o "$OUT/$name" "$url"; then
    echo "     !! FAILED: $name" >&2
    fail=$((fail+1))
  fi
done

echo
if [ "$fail" -eq 0 ]; then
  echo "Done. All ${#assets[@]} files saved to ./$OUT/"
else
  echo "Done with $fail failure(s). Re-run to retry — existing files are overwritten." >&2
  exit 1
fi
