--liquibase formatted sql

--changeset liquibase:1
CREATE SCHEMA IF NOT EXISTS secr_data;

--changeset liquibase:2
CREATE TABLE IF NOT EXISTS secr_data.processed_data_item (
    id SERIAL PRIMARY KEY,
    company_id text NOT NULL,
    source_id text NOT NULL,
    line_item_number integer NOT NULL,
    source_type text,
    associated_facility text,
    supplier text,
    category text,
    fuel_type text,
    vehicle_type text,
    vehicle_fuel_type text,
    transport_type text NULL DEFAULT 'CAR',
    original_value numeric,
    original_unit text,
    unit_conversion_factor_used numeric,
    converted_value numeric,
    converted_unit text,
    scope integer,
    conversion_factor_identifier text,
    emission_conversion_factor_used numeric,
    kg_co2e_total_value numeric,
    energy_conversion_factor_used numeric,
    kwh_value numeric,
    wtt_conversion_factor_used numeric,
    kg_co2e_wtt_value numeric,
    kg_co2e_co2_value numeric,
    kg_co2e_ch4_value numeric,
    kg_co2e_n2o_value numeric,
    start_date date,
    end_date date,
    status text,
    custom_emission_factor numeric,
    custom_measurement numeric,
    custom_measurement_unit text,
    
    UNIQUE (company_id, source_id, line_item_number)
);

--changeset liquibase:3
CREATE TABLE IF NOT EXISTS secr_data.supplier_data (
    id SERIAL PRIMARY KEY,
    purchase_id TEXT,
    supplier_name TEXT NOT NULL,
    supplier_email TEXT ,
    supplier_category TEXT,
    impact TEXT,
    spend TEXT,
    primary_spend_category TEXT,
    default_emission_factor TEXT,
    override_emission_factor TEXT,
    emission_factor_source TEXT,
    emission_source TEXT,
    total_emissions NUMERIC,
    total_calculated_emissions NUMERIC,
    score NUMERIC,
    status TEXT,
    date DATE NOT NULL,
    is_published BOOLEAN DEFAULT FALSE,
    emissions NUMERIC,
    supplier_information JSONB  -- For storing JSON data in PostgreSQL
);