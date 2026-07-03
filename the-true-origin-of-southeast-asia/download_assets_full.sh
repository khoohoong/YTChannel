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
  # N1a regenerated 2026-07-03 — original (fd69c041...) had a visual glitch, replaced.
  "N1a_flores_island_aerial.mp4|$BASE/hf_20260703_130014_4186bdc9-c906-4a07-8b0b-af30d4722990.mp4"
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

  # ---------- SECOND B-ROLL BATCH: FLORES ----------
  "N1f_stone_tool_macro.mp4|$BASE/hf_20260702_144836_925aaae7-4b59-444f-9efd-c259ddb9d429.mp4"
  "N1g_flores_coastline.mp4|$BASE/hf_20260702_144841_48ee2b84-3fbf-4780-a6e2-f698aa7b3cca.mp4"
  "N1h_excavation_grid.mp4|$BASE/hf_20260702_144844_bcab66fb-f83d-417a-b1b6-fac3c66ca8b0.mp4"
  "N1i_floresiensis_walking.mp4|$BASE/hf_20260702_144852_c2225433-af86-4ba3-8ccb-34580c34fca3.mp4"
  "N1j_rainforest_sunbeams.mp4|$BASE/hf_20260702_144903_613cd13e-eb4d-4e58-b82d-3794dbcb3a72.mp4"

  # ---------- SECOND B-ROLL BATCH: AUSTRONESIAN ----------
  "N2e_crabclaw_sail.mp4|$BASE/hf_20260702_145027_2b283a35-128f-4147-a9b2-aca5a8515ab8.mp4"
  "N2f_stern_wake.mp4|$BASE/hf_20260702_144912_a8aa42ab-d4ac-475e-a0c4-3c1c7c3c3efc.mp4"
  "N2g_island_landfall.mp4|$BASE/hf_20260702_145033_bea245bc-4cd5-4357-ba25-b0a22ee0bd34.mp4"
  "N2h_rice_terraces.mp4|$BASE/hf_20260702_145102_0025f8cc-b007-41a4-8b56-a6a7b55b42c4.mp4"

  # ---------- SECOND B-ROLL BATCH: NAGA ----------
  "N3e_churning_ocean_relief.mp4|$BASE/hf_20260702_144924_fe66154f-112d-4619-80f2-1b9c359d6739.mp4"
  "N3f_monsoon_rain_river.mp4|$BASE/hf_20260702_144928_214431eb-6ff9-40c9-b1f9-e4f3f561bea3.mp4"
  "N3g_floating_candles.mp4|$BASE/hf_20260702_144932_c49ee8b8-84bb-4fd1-85a3-f56c72d023bf.mp4"
  "N3h_naga_head_macro.mp4|$BASE/hf_20260702_144935_5e2f4d4e-a75e-4f15-82ea-34a132edcd66.mp4"

  # ---------- SECOND B-ROLL BATCH: ANGKOR ----------
  "N4f_wat_silhouette_sunrise.mp4|$BASE/hf_20260702_144938_aed7831c-1cac-404e-919a-6fc27a47aef3.mp4"
  "N4g_apsara_macro.mp4|$BASE/hf_20260702_144944_59dae0e0-b01b-48d2-88f8-9b2fe25d8ef5.mp4"
  "N4h_drought_cracked_earth.mp4|$BASE/hf_20260702_144947_ebc0111c-3d7f-4160-bf9c-2ccb93d32c7c.mp4"
  "N4i_monks_causeway.mp4|$BASE/hf_20260702_145043_404d13b4-186a-4998-8cdf-1dc0dafdecd4.mp4"
  "N4j_complex_pullback.mp4|$BASE/hf_20260702_144952_f0478987-d824-4919-b3ef-e9c19cd3ec67.mp4"

  # ---------- THIRD B-ROLL BATCH: FLORES (full 1x coverage, 2026-07-03) ----------
  "P1a_excavation_pit_wide.mp4|$BASE/hf_20260703_085715_3ccbd67d-e757-4f48-9402-da897cb0019c.mp4"
  "P1b_sieving_sediment.mp4|$BASE/hf_20260703_085312_0f0a7e4e-bd41-4e3d-8865-b1f1c6858b9c.mp4"
  "P1c_field_notebook_calipers.mp4|$BASE/hf_20260703_085317_9b7230af-924c-4a69-876b-c37468cbcf58.mp4"
  "P1d_headlamp_cave_wall.mp4|$BASE/hf_20260703_085320_9e55ea9b-9141-469f-8925-4bf0e068d90a.mp4"
  "P1e_stalactites_pool.mp4|$BASE/hf_20260703_085327_2589eb15-4a25-4082-a218-03375e5d12eb.mp4"
  "P1f_floresiensis_hand_tool.mp4|$BASE/hf_20260703_085331_b051da7f-d3fd-4b32-9adc-34cdca26559c.mp4"
  "P1g_komodo_dragon.mp4|$BASE/hf_20260703_085339_d0864116-ff1d-435d-bc0f-7e232c05acca.mp4"
  "P1h_flores_crater_aerial.mp4|$BASE/hf_20260703_085349_01f56d1a-7422-4111-af92-84b126b82c99.mp4"
  "P1i_bones_lab_table.mp4|$BASE/hf_20260703_085353_3913d3ef-83c2-48b0-a127-37154dbcf29c.mp4"
  "P1j_giant_rat.mp4|$BASE/hf_20260703_085356_5ce4b318-c844-401b-baba-7bf06051aac2.mp4"
  "P1k_storm_clouds_karst.mp4|$BASE/hf_20260703_085721_8c4e330c-8ff3-4743-a9da-25eea8a422f5.mp4"
  "P1l_karst_timelapse.mp4|$BASE/hf_20260703_085401_567e712e-c79e-456a-9140-4efa3abc75c4.mp4"

  # ---------- THIRD B-ROLL BATCH: AUSTRONESIAN ----------
  "P2a_navigator_hand_stars.mp4|$BASE/hf_20260703_085405_ca1ceb1c-ffc4-49cb-9209-472bc8cce4c3.mp4"
  "P2b_paddlers_rowing.mp4|$BASE/hf_20260703_085413_244f6d01-c005-45c4-8ef7-5611c055b88e.mp4"
  "P2c_canoe_storm_swell.mp4|$BASE/hf_20260703_085416_e89cb9fb-7f43-4532-8fe0-204c029e4478.mp4"
  "P2d_dolphins_hull.mp4|$BASE/hf_20260703_085421_447eb43d-8e40-4c9c-bcc6-46320dc904e8.mp4"
  "P2e_family_cargo_canoe.mp4|$BASE/hf_20260703_085423_07330efb-f61b-407a-91e5-a2a85220d634.mp4"
  "P2f_lapita_pottery.mp4|$BASE/hf_20260703_085642_06731ca3-2669-4154-ac6e-53de491b8c34.mp4"
  "P2g_tattooed_navigator_portrait.mp4|$BASE/hf_20260703_085646_fd638d3d-e508-4c7c-8172-26dfe02cd6e3.mp4"
  "P2h_canoe_ashore_footprints.mp4|$BASE/hf_20260703_085725_90ddfcfc-592d-47fa-8999-02dc267ebcbd.mp4"

  # ---------- THIRD B-ROLL BATCH: NAGA ----------
  "P3a_underwater_serpent_shadow.mp4|$BASE/hf_20260703_085731_7420e428-b735-43b8-847f-e350364f7d19.mp4"
  "P3b_naga_temple_mural.mp4|$BASE/hf_20260703_085739_e3009658-cb77-46fb-8455-20b7dfede9d9.mp4"
  "P3c_buddha_naga_hood.mp4|$BASE/hf_20260703_085743_de85c106-e47b-43ec-8a92-08428d1a2f58.mp4"
  "P3d_monk_incense_riverside.mp4|$BASE/hf_20260703_085747_1754e33d-c0fa-447c-b913-f45061026fef.mp4"
  "P3e_king_cobra.mp4|$BASE/hf_20260703_085755_e4f1bffc-e71f-4ffe-b459-e84359c02907.mp4"
  "P3f_mekong_delta_aerial.mp4|$BASE/hf_20260703_085759_25b348a1-7169-426d-925e-b403242d90a1.mp4"
  "P3g_lightning_over_river.mp4|$BASE/hf_20260703_085805_1601df93-1293-4169-bf55-5f6d7e1d4d87.mp4"
  "P3h_fisherman_net_dawn.mp4|$BASE/hf_20260703_085812_4415cf18-62ab-4643-a02e-9acb1c5b52f3.mp4"

  # ---------- THIRD B-ROLL BATCH: ANGKOR ----------
  "P4a_stonemasons_carving.mp4|$BASE/hf_20260703_085927_e9ff6849-53bb-4c2b-b367-87b94a9f43f6.mp4"
  "P4b_elephants_hauling_stone.mp4|$BASE/hf_20260703_085822_30b486c0-e183-4d0c-abd3-9db755358654.mp4"
  "P4c_long_colonnade_corridor.mp4|$BASE/hf_20260703_085932_7b854bcf-91ab-4cff-a5af-a9d8511f2fc5.mp4"
  "P4d_dim_inner_sanctum.mp4|$BASE/hf_20260703_085834_b13e7af6-016a-44a7-b6d6-777fb8d04bb0.mp4"
  "P4e_lotus_pond_towers.mp4|$BASE/hf_20260703_085935_c3fc609c-404c-45fd-be38-7b1255170d10.mp4"
  "P4f_devata_macro.mp4|$BASE/hf_20260703_085839_c4299a4b-001f-4ffd-9e53-5caa7cc887d6.mp4"
  "P4g_monk_silhouette_sunset.mp4|$BASE/hf_20260703_085842_05cd8b47-96a0-4553-a201-e22cb09b2a04.mp4"
  "P4h_angkor_thom_gate_aerial.mp4|$BASE/hf_20260703_085848_b26dfd11-013b-4c89-88d8-b72e6cf77d78.mp4"
  "P4i_rain_temple_stone.mp4|$BASE/hf_20260703_085851_9a8301ac-89f9-424b-8bca-2453aaba429c.mp4"
  "P4j_star_trails_towers.mp4|$BASE/hf_20260703_085855_fddb61c4-63cf-46ee-a469-8dab335a3c12.mp4"
  "P4k_toppled_stones_ruin.mp4|$BASE/hf_20260703_085858_9f4175e3-a0dc-4cf7-a239-b140dad2dfba.mp4"
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
