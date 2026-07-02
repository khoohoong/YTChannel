#!/usr/bin/env bash
#
# Download ALL assets for the full ~9:06 cut of
# "The TRUE Origin of Southeast Asia"
# Usage:  bash download_assets_full.sh
# Files land in ./sea_full_assets/ , named in edit order per segment.
#
set -euo pipefail

OUT="sea_full_assets"
mkdir -p "$OUT"
BASE="https://d8j0ntlcm91z4.cloudfront.net/user_30b7CTGiTTJpfv3eHgP4QQtBJ1y"

assets=(
  # ---------- VOICEOVER (Arthur / ElevenLabs) ----------
  "VO-A_coldopen_flores.mp3|$BASE/hf_20260702_143348_8378f7cf-fe43-4b9f-8a50-9f50ff89cf3d.mp3"
  "VO-B_austronesian.mp3|$BASE/hf_20260702_143413_f956fd3f-19cc-44ad-8ef8-956a4ddd35d8.mp3"
  "VO-C_naga.mp3|$BASE/hf_20260702_143423_0005f042-661e-4bb7-9a4d-04ee13d8c092.mp3"
  "VO-D_angkor_outro.mp3|$BASE/hf_20260702_143429_265695f1-5e91-4342-9632-14e755941723.mp3"

  # ---------- HEROES (Seedance, reused) ----------
  "H1_flores_cave.mp4|$BASE/hf_20260624_140131_2891a779-7103-4472-af60-2d072f590bbf.mp4"
  "H2_canoe_fleet_night.mp4|$BASE/hf_20260624_140133_e1be8710-2bf9-48e2-a4bb-b22f5d27dd41.mp4"
  "H3_naga_rising.mp4|$BASE/hf_20260624_140144_84c61760-ac5e-461a-80d3-08cb0459d02c.mp4"
  "H4_angkor_aerial.mp4|$BASE/hf_20260624_140146_3af63dee-b91b-4713-9525-74f765aff51e.mp4"

  # ---------- STILLS (Nano Banana, reused) ----------
  "S1_floresiensis_bust.png|$BASE/hf_20260625_053250_66842ddd-855e-41a2-84d3-4dec0fc55078.png"
  "S2_navigator_stars.png|$BASE/hf_20260625_053330_cfc6c069-544b-45d8-84b2-ce63b082ffa9.png"
  "S3_naga_sculpture.png|$BASE/hf_20260625_053334_28cfa547-b75d-4ef0-b89a-eba3235d4b4a.png"
  "S4_angkor_basrelief.png|$BASE/hf_20260625_053337_1f09bd94-e826-48f0-9b7a-e61bcded241d.png"

  # ---------- OLD B-ROLL (Kling, reused) ----------
  "OB1_hands_bone.mp4|$BASE/hf_20260625_053340_6e72ddfb-085a-49a5-adfd-50d875cc8f8e.mp4"
  "OB2_canoe_prow.mp4|$BASE/hf_20260625_053342_5e3cf631-02b9-4b11-90d5-6ec530b982f6.mp4"
  "OB3_misty_river.mp4|$BASE/hf_20260625_053345_be189de9-1c5b-4a9e-8573-ffee0db9e938.mp4"
  "OB4_monk_corridor.mp4|$BASE/hf_20260625_053355_410a7799-ecfc-4a7c-a4f3-10c1a7672aae.mp4"

  # ---------- NEW B-ROLL: FLORES ----------
  "N1a_flores_island_aerial.mp4|$BASE/hf_20260702_143624_fd69c041-feb7-4ada-9eda-3b5e00882601.mp4"
  "N1b_liangbua_cave_mouth.mp4|$BASE/hf_20260702_143628_f9b97547-2c59-4339-ae2d-7a7e3325b0c7.mp4"
  "N1c_skull_scale.mp4|$BASE/hf_20260702_143456_e0a9f3c7-e7a1-4f4f-8f3d-9ee614d33102.mp4"
  "N1d_stegodon_dusk.mp4|$BASE/hf_20260702_143501_a1b19c84-e6d8-4fe8-8c79-ecfe2f020065.mp4"
  "N1e_knapping_fire.mp4|$BASE/hf_20260702_143509_bfb219d3-dad6-409e-a9c2-bbd2fcf05723.mp4"

  # ---------- NEW B-ROLL: AUSTRONESIAN ----------
  "N2a_lone_canoe_aerial.mp4|$BASE/hf_20260702_143514_64b2c8a4-34b4-4934-864e-fe3b6e6c9401.mp4"
  "N2b_hands_lashing_hull.mp4|$BASE/hf_20260702_143519_87ac87af-786e-4cdf-9a0c-fbfa331a90af.mp4"
  "N2c_milky_way.mp4|$BASE/hf_20260702_143523_aa6e99a8-706a-4a1a-a7f3-efcb5ce28c72.mp4"
  "N2c_milky_way_ALT.mp4|$BASE/hf_20260702_143636_dd9926b1-d0fb-4112-87d6-c9aadfbb4f36.mp4"
  "N2d_seabirds.mp4|$BASE/hf_20260702_143533_2482f4d4-7a57-42f0-ac1e-cbe56df7b161.mp4"

  # ---------- NEW B-ROLL: NAGA ----------
  "N3a_naga_balustrade.mp4|$BASE/hf_20260702_143537_3dade034-b656-4f5c-98be-a21b142aa66e.mp4"
  "N3b_naga_staircase.mp4|$BASE/hf_20260702_143541_95cb121f-b3a0-48f1-98cf-430bbbbfd3d4.mp4"
  "N3c_naga_fireballs.mp4|$BASE/hf_20260702_143641_e53cd3cb-4920-4c73-81d0-29cb4ef94ea0.mp4"
  "N3d_royal_barge.mp4|$BASE/hf_20260702_143547_f26b49e0-6d4f-44d9-9511-6789a64e22ec.mp4"

  # ---------- NEW B-ROLL: ANGKOR ----------
  "N4a_wat_moat_reflection.mp4|$BASE/hf_20260702_143731_609ea6da-1f75-4390-8e28-8566aa6e7137.mp4"
  "N4b_basrelief_tracking.mp4|$BASE/hf_20260702_143555_c97e1fba-e1e8-4a81-a345-b3bcd5111b90.mp4"
  "N4c_baray_aerial.mp4|$BASE/hf_20260702_143600_ccf01950-2909-4937-b81c-8515776dd4c7.mp4"
  "N4d_taprohm_roots.mp4|$BASE/hf_20260702_143606_66d732ed-9dae-49a5-a1ea-246cc4abdd1b.mp4"
  "N4e_bayon_faces.mp4|$BASE/hf_20260702_143609_78ecf9fa-e785-435a-a9df-c1b05d0268ca.mp4"
)

echo "Downloading ${#assets[@]} assets into ./$OUT/ ..."
fail=0
for entry in "${assets[@]}"; do
  name="${entry%%|*}"; url="${entry#*|}"
  printf '  -> %s\n' "$name"
  curl -fSL --retry 4 --retry-delay 2 -o "$OUT/$name" "$url" || { echo "  !! FAILED: $name" >&2; fail=$((fail+1)); }
done
echo
[ "$fail" -eq 0 ] && echo "Done. All ${#assets[@]} files in ./$OUT/" || { echo "Done with $fail failure(s); re-run to retry." >&2; exit 1; }
