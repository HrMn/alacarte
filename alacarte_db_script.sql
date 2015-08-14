
CREATE OR REPLACE FUNCTION update_modified_column()
  RETURNS trigger AS
  $$
BEGIN
    NEW.modified = now();
    RETURN NEW;	
END;
$$ LANGUAGE plpgsql;


CREATE TABLE tables
(
  id serial NOT NULL,
  name character varying(30),
  created timestamp without time zone DEFAULT now(),
  modified timestamp without time zone DEFAULT now(),
  CONSTRAINT tables_pkey PRIMARY KEY (id)
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON tables
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();

CREATE TABLE user_roles
(
  id serial NOT NULL,
  role_name character varying(30) NOT NULL,
  created timestamp without time zone DEFAULT now(),
  modified timestamp without time zone DEFAULT now(),
  CONSTRAINT user_roles_pkey PRIMARY KEY (id)
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON user_roles
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();

CREATE TABLE users
(
  id serial NOT NULL,
  username character varying(30),
  password character varying(30),
  email character varying(60),
  role integer NOT NULL,
  created timestamp without time zone DEFAULT now(),
  modified timestamp without time zone DEFAULT now(),
  CONSTRAINT users_pkey PRIMARY KEY (id),
  CONSTRAINT users_role_fkey FOREIGN KEY (role)
      REFERENCES user_roles (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON users
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();


CREATE TABLE category
(
  id serial NOT NULL,
  name character varying(100) NOT NULL,
  description character varying(500),
  image_url character varying(200),
  created timestamp without time zone DEFAULT now(),
  modified timestamp without time zone DEFAULT now(),
  CONSTRAINT category_pkey PRIMARY KEY (id)
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON category
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();


CREATE TABLE sub_category
(
  id serial NOT NULL,
  name character varying(100) NOT NULL,
  description character varying(500),
  image_url character varying(200),
  category_id smallint NOT NULL,
  created timestamp without time zone DEFAULT now(),
  modified timestamp without time zone DEFAULT now(),
  CONSTRAINT sub_category_pkey PRIMARY KEY (id),
  CONSTRAINT sub_category_category_id_fkey FOREIGN KEY (category_id)
      REFERENCES category (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON sub_category
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();

CREATE TABLE food_items
(
  id serial NOT NULL,
  name character varying(100) NOT NULL,
  description character varying(500),
  image_url character varying(200),
  category_id smallint NOT NULL,
  sub_category_id smallint,
  rating smallint DEFAULT (-1),
  ingredients json,
  best_combination json,
  rate numeric,
  CONSTRAINT food_items_pkey PRIMARY KEY (id),
  CONSTRAINT food_items_category_id_fkey FOREIGN KEY (category_id)
      REFERENCES category (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON food_items
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();



CREATE TABLE orders
(
  id serial NOT NULL,
  table_id smallint NOT NULL,
  waiter_id smallint,
  chef_id smallint,
  order_details json,
  order_status character varying(100),
  cost numeric(50,0),
  CONSTRAINT orders_pkey PRIMARY KEY (id),
  CONSTRAINT orders_chef_id_fkey FOREIGN KEY (chef_id)
      REFERENCES users (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT orders_table_id_fkey FOREIGN KEY (table_id)
      REFERENCES tables (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT orders_waiter_id_fkey FOREIGN KEY (waiter_id)
      REFERENCES users (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TRIGGER update_modtime
  BEFORE UPDATE
  ON orders
  FOR EACH ROW
  EXECUTE PROCEDURE update_modified_column();

