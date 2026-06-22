# 📋 Proyek Akhir Manajemen Proses Bisnis — Kelompok 4

## Penerapan BPM Lifecycle pada Proses Koordinator Program Studi di FIK UPNVJ

Menggunakan **Camunda Modeler 5.44.0** dan **CIB seven BPMS 2.2.0**

---

### 👥 Anggota Kelompok

| No | Nama | NIM |
|----|------|-----|
| 1 | Callysta Cendikia Diba P | 2310512079 |
| 2 | Ahmad Rifqi Abduh Falah | 2310512091 |
| 3 | Vega Setiawan | 2310512108 |
| 4 | Muhammad Arya Yudha | 2310512123 |

**Dosen Pengampu:** I Wayan Widi Pradnyana, M.TI  
**Program Studi:** S1 Sistem Informasi, FIK UPNVJ  
**Semester:** Genap 2025/2026

---

### 📌 Studi Kasus

Analisis dan perbaikan 4 proses bisnis utama **Koordinator Program Studi (Korprodi) S1 Sains Data** di FIK UPNVJ berdasarkan wawancara dengan **Novi Trisman Hadi, S.Pd., M.Kom.**

| Kode | Proses | Deskripsi |
|------|--------|-----------|
| P1 | Penentuan Dosen Pengampu MK | Plotting dosen ke mata kuliah berdasarkan kompetensi dan ketersediaan |
| P2 | Pemilihan Dosen Pembimbing TA | Pengajuan dan penunjukan pembimbing tugas akhir mahasiswa |
| P3 | Pemantauan Masa Studi Mahasiswa | Early warning system berbasis tier untuk deteksi mahasiswa kritis |
| P4 | Pembuatan RPS via SIMPEL | Penyusunan dan verifikasi 3 level (Korprodi → GKM → Wadek 1) |

---

### 🔄 Pendekatan BPM Lifecycle
Discovery → Analysis → Design → Implementation → Monitoring → Improvement

---

### 🛠️ Tech Stack

| Komponen | Spesifikasi |
|----------|-------------|
| BPMN Modeler | Camunda Modeler 5.44.0 |
| BPMS Engine | CIB seven BPMS 2.2.0 |
| Server | Ubuntu 24.04 LTS (Docker) |
| URL | `cibseven2.foul.one` |
| Notifikasi | Discord Webhook via HTTP Connector |
| Java | OpenJDK 17 |

---

### 📊 Hasil Implementasi

| Komponen | Jumlah |
|----------|--------|
| File BPMN | 8 (4 as-is + 4 to-be) |
| File DMN | 1 (aktif terhubung BRT di P3) |
| File Form | 30 (.form external JSON) |
| Business Rule Task | 1 (P3 — Tier Classification) |
| Embedded Subprocess | 1 (P4 — Penyusunan Draft RPS) |
| Boundary Timer Event | 3 (P1, P2, P4) |
| User Aktif CIB seven | 5 (novikps, gkm4, erlywadek, adrezo, vegamhs) |
| Candidate Groups | 5 (KPS, Dosen, Mahasiswa, Pimpinan, camunda-admin) |

---

### 🧪 Hasil Simulasi

10 skenario pengujian — **172 total activities** — semua COMPLETED

| Skenario | Proses | Activities | Status |
|----------|--------|-----------|--------|
| 1A Normal | P1 | 16 | ✅ Completed |
| 1B Violation | P1 | 18 | ✅ Completed |
| 1C Timer Eskalasi | P1 | 20 | ✅ Completed |
| 2A Normal | P2 | 14 | ✅ Completed |
| 2B Tidak Eligible | P2 | 5 | ✅ Completed |
| 2C Timer Eskalasi | P2 | 16 | ✅ Completed |
| 3A Tier 0 (Sem 6) | P3 | 2 | ✅ Completed |
| 3B Tier 1 (Sem 10) | P3 | 8 | ✅ Completed |
| 3C Tier 3 (Sem 14) | P3 | 11 | ✅ Completed |
| 4A Normal + Revisi | P4 | 63 | ✅ Completed |

**DMN Decision Instance:**

| Input (Semester) | Output (Tier) | Klasifikasi |
|-----------------|---------------|-------------|
| 6 | 0 | Normal |
| 10 | 1 | Warning |
| 12 | 2 | Critical |
| 14 | 3 | Terminal |

---

### 🔑 Fitur Utama To-Be

- **Auto-suggest plotting** berbasis kompetensi dosen (P1)
- **Gateway eligibilitas otomatis** — cek SKS + UKT + MK prasyarat sebelum PA (P2)
- **DMN Tiered Early Warning** — klasifikasi tier 0-3 otomatis via Business Rule Task (P3)
- **Embedded Subprocess** — Penyusunan Draft RPS dengan boundary timer SLA (P4)
- **Boundary Timer Event** — eskalasi otomatis jika aktor tidak respons (P1: 2 hari, P2: 3 hari)
- **Retry Counter** — mencegah infinite loop pada assign dosen (P1) dan cari pembimbing (P2), max 3x
- **Discord Webhook** — notifikasi real-time di setiap event proses via HTTP Connector
- **External Form (.form)** — 30 file JSON form terpisah dari BPMN, migrasi dari embedded formData

---

### 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik mata kuliah Manajemen Proses Bisnis, FIK UPNVJ.