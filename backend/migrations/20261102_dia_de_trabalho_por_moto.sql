ALTER TABLE dia_de_trabalho
    DROP CONSTRAINT IF EXISTS dia_de_trabalho_data_trabalhada_key;

ALTER TABLE dia_de_trabalho
    DROP CONSTRAINT IF EXISTS uq_dia_de_trabalho_moto_data;

ALTER TABLE dia_de_trabalho
    ADD CONSTRAINT uq_dia_de_trabalho_moto_data
    UNIQUE (moto_id, data_trabalhada);
