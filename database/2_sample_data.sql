
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE analysis_results;
TRUNCATE TABLE sites;
SET FOREIGN_KEY_CHECKS = 1;



INSERT INTO sites (site_name, latitude, longitude, area_sqm, solar_irradiance_kwh, grid_distance_km, slope_degrees, road_distance_km, elevation_m, land_type, region) VALUES
('Periyanaickenpalayam Site', 11.0765, 76.9872, 45000, 5.8, 2.5, 3.2, 0.8, 425, 'Agricultural', 'Tamil Nadu'),
('Avinashi Industrial Zone', 11.1936, 77.2686, 62000, 5.6, 1.2, 1.8, 0.3, 380, 'Industrial', 'Tamil Nadu'),
('Tiruppur North Field', 11.1271, 77.3661, 38000, 5.7, 4.8, 5.1, 1.2, 295, 'Agricultural', 'Tamil Nadu'),
('Udumalpet Solar Park', 10.5857, 77.2486, 78000, 6.1, 0.8, 2.1, 0.5, 515, 'Wasteland', 'Tamil Nadu'),
('Pollachi East Zone', 10.6689, 77.0448, 52000, 5.9, 3.2, 4.5, 1.8, 325, 'Agricultural', 'Tamil Nadu'),
('Valparai Valley Site', 10.3269, 76.9511, 15000, 4.2, 12.5, 15.8, 4.2, 1180, 'Hilly', 'Tamil Nadu'),
('Coimbatore Tech Park', 11.0168, 76.9558, 28000, 5.4, 1.5, 2.8, 0.4, 415, 'Industrial', 'Tamil Nadu'),
('Mettupalayam Plains', 11.3021, 76.9407, 68000, 5.8, 2.1, 1.2, 0.9, 335, 'Agricultural', 'Tamil Nadu'),
('Sulur Airbase Adjacent', 11.0244, 77.1686, 95000, 6.2, 0.5, 0.8, 0.2, 405, 'Open Land', 'Tamil Nadu'),
('Annur Rural Site', 11.2356, 77.1062, 42000, 5.5, 5.5, 6.2, 2.1, 385, 'Agricultural', 'Tamil Nadu'),
('Kinathukadavu South', 10.7708, 77.0272, 55000, 6.0, 1.8, 2.5, 0.7, 445, 'Wasteland', 'Tamil Nadu'),
('Madukkarai Junction', 10.9115, 76.9626, 48000, 5.6, 3.8, 4.1, 1.5, 380, 'Mixed Use', 'Tamil Nadu'),
('Karamadai Forest Edge', 11.2419, 76.9619, 25000, 5.1, 8.2, 9.5, 3.5, 515, 'Forest Adjacent', 'Tamil Nadu'),
('Negamam Agricultural', 11.0456, 77.2914, 72000, 5.9, 1.9, 1.5, 0.6, 365, 'Agricultural', 'Tamil Nadu'),
('Thondamuthur Reservoir', 11.0029, 76.8372, 38000, 5.4, 6.5, 7.8, 2.8, 525, 'Near Water Body', 'Tamil Nadu'),
('Sarkarsamakulam Plains', 11.1889, 77.4261, 82000, 6.1, 1.1, 1.9, 0.4, 295, 'Agricultural', 'Tamil Nadu'),
('Palladam Town Outskirts', 10.9989, 77.2861, 44000, 5.7, 4.2, 3.8, 1.4, 340, 'Peri-Urban', 'Tamil Nadu'),
('Kangeyam Industrial', 10.9889, 77.5628, 58000, 5.8, 2.8, 2.2, 0.9, 285, 'Industrial', 'Tamil Nadu'),
('Dharapuram Solar Field', 10.7378, 77.5361, 65000, 6.0, 1.5, 1.1, 0.5, 265, 'Open Land', 'Tamil Nadu'),
('Vellakoil Eastern Tract', 10.9414, 77.7161, 48000, 5.9, 3.5, 3.2, 1.2, 275, 'Agricultural', 'Tamil Nadu'),
('Erode Border Zone', 11.3422, 77.7167, 52000, 5.7, 2.9, 2.8, 1.0, 245, 'Mixed Use', 'Tamil Nadu'),
('Bhavani Riverside', 11.4456, 77.6806, 35000, 5.5, 5.8, 4.5, 2.2, 185, 'Near Water Body', 'Tamil Nadu'),
('Sathyamangalam Hills', 11.5089, 77.2361, 18000, 4.8, 15.2, 18.5, 5.5, 825, 'Hilly', 'Tamil Nadu'),
('Gobichettipalayam Field', 11.4556, 77.4431, 71000, 6.0, 1.6, 1.4, 0.6, 255, 'Agricultural', 'Tamil Nadu'),
('Anthiyur Rural Area', 11.5761, 77.5931, 46000, 5.8, 4.5, 5.8, 1.9, 315, 'Agricultural', 'Tamil Nadu'),
('Chennimalai Textile Zone', 11.1644, 77.6036, 39000, 5.6, 3.9, 3.5, 1.3, 285, 'Industrial', 'Tamil Nadu'),
('Perundurai Junction', 11.2750, 77.5878, 54000, 5.8, 2.4, 2.1, 0.8, 265, 'Mixed Use', 'Tamil Nadu'),
('Vijayamangalam Site', 11.4956, 77.5544, 62000, 5.9, 1.9, 1.7, 0.7, 275, 'Open Land', 'Tamil Nadu'),
('Ingur Dam Adjacent', 11.3889, 77.0556, 28000, 5.3, 7.8, 8.2, 3.1, 465, 'Near Water Body', 'Tamil Nadu'),
('Sirumugai Wildlife Border', 11.3206, 76.6911, 22000, 5.0, 11.5, 12.8, 4.5, 685, 'Forest Adjacent', 'Tamil Nadu'),
('Podanur Railway Zone', 10.9858, 76.9731, 41000, 5.6, 3.2, 3.8, 1.1, 395, 'Industrial', 'Tamil Nadu'),
('Sundakkamuthur Field', 11.0231, 77.0989, 58000, 5.8, 2.2, 1.8, 0.7, 375, 'Agricultural', 'Tamil Nadu'),
('Vellalore Lake Side', 10.9456, 76.8978, 32000, 5.4, 6.2, 5.5, 2.4, 445, 'Near Water Body', 'Tamil Nadu'),
('Narasimhanaickenpalayam', 11.2089, 77.1578, 67000, 6.0, 1.4, 1.3, 0.5, 355, 'Agricultural', 'Tamil Nadu'),
('Karumathampatti North', 11.0456, 77.0061, 49000, 5.7, 3.6, 4.2, 1.4, 405, 'Mixed Use', 'Tamil Nadu'),
('Chinnavedampatti Site', 10.9567, 76.9228, 55000, 5.8, 2.7, 2.5, 0.9, 415, 'Open Land', 'Tamil Nadu'),
('Thondamuthur Hills', 10.9789, 76.8156, 19000, 4.9, 13.8, 16.2, 4.8, 625, 'Hilly', 'Tamil Nadu'),
('Chettipalayam Plains', 11.0789, 77.1456, 74000, 6.1, 1.2, 1.1, 0.4, 365, 'Agricultural', 'Tamil Nadu'),
('Ganapathy Industrial', 11.0456, 76.9689, 36000, 5.5, 4.5, 3.9, 1.5, 425, 'Industrial', 'Tamil Nadu'),
('Idigarai Border Site', 10.8878, 76.9456, 63000, 5.9, 2.0, 1.9, 0.7, 385, 'Open Land', 'Tamil Nadu'),
('Malumichampatti East', 11.0978, 77.2267, 51000, 5.7, 3.1, 2.9, 1.0, 345, 'Agricultural', 'Tamil Nadu'),
('Kaniyur Rural Tract', 11.0089, 77.3456, 68000, 5.9, 1.7, 1.5, 0.6, 325, 'Agricultural', 'Tamil Nadu'),
('Kurichi Lake Zone', 11.0234, 76.9356, 29000, 5.3, 7.1, 6.8, 2.7, 435, 'Near Water Body', 'Tamil Nadu'),
('Veerapandi Junction', 10.9345, 77.4567, 56000, 5.8, 2.5, 2.3, 0.8, 315, 'Mixed Use', 'Tamil Nadu'),
('Oddarpalayam Field', 11.0867, 77.3789, 72000, 6.0, 1.5, 1.2, 0.5, 335, 'Open Land', 'Tamil Nadu'),
('Perur Temple Adjacent', 11.0245, 76.9123, 33000, 5.4, 5.5, 5.2, 2.0, 445, 'Peri-Urban', 'Tamil Nadu'),
('Somayampalayam Site', 11.0678, 77.1834, 61000, 5.9, 2.1, 1.8, 0.7, 365, 'Agricultural', 'Tamil Nadu'),
('Madvarayapuram Zone', 11.1234, 77.2567, 47000, 5.6, 3.8, 3.6, 1.3, 355, 'Mixed Use', 'Tamil Nadu'),
('Saravanampatti Tech Hub', 11.0767, 76.9956, 42000, 5.5, 4.2, 4.0, 1.4, 415, 'Industrial', 'Tamil Nadu'),
('Thudiyalur Eastern Site', 11.0556, 77.0456, 69000, 6.0, 1.8, 1.6, 0.6, 385, 'Open Land', 'Tamil Nadu');

CALL calculate_suitability_scores();