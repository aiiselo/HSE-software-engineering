create function create_database()
	returns void language sql as $$
		create table if not exists "Publisher"(
			name text primary key not null,
			telephone text not null,
			lastUpdate timestamptz default current_timestamp not null
		);
		create table if not exists "Book"(
			id integer primary key not null generated always as identity,
			title text not null,
			author text not null,
			publisher text not null
		);
		create index if not exists author on "Book" (author);

		create or replace function update_time()
			returns trigger as $u$
			begin 
				new.lastUpdate = current_timestamp;
				return new;
			end;
		$u$ language plpgsql;

		drop trigger if exists trigger_update on "Publisher";

		create trigger trigger_update before update on "Publisher" 
			for row execute procedure update_time();
$$;

select "create_database"();

create function get_publishers()
	returns json language plpgsql as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Publisher".name,
				'telephone', "Publisher".telephone,
				'lastUpdate', "Publisher".lastUpdate
				)) from "Publisher");
		end
	$$;

create function get_books() 
	returns json language plpgsql as $$
		begin 
			return (select json_agg(json_build_object(
				'id', "Book".id,
				'title', "Book".title,
				'author', "Book".author,
				'publisher', "Book".publisher
				)) from "Book");
		end
	$$;

create function add_to_publisher(in name text, in telephone text)
	returns void language sql as $$
		insert into "Publisher"(name, telephone) values (name, telephone)
	$$;

create function add_to_book(in title text, in author text, in publisher text)
	returns void language sql as $$
		insert into "Book"(title, author, publisher) values (title, author, publisher)
	$$;

create function clear_publishers() 
	returns void language sql as $$ 
		truncate "Publisher"
	$$;

create function clear_books()
	returns void language sql as $$ 
		truncate "Book"
	$$;

create function clear_all()
	returns void language sql as $$ 
		truncate "Publisher";
		truncate "Book"
	$$;

create function find_book(in query text) 
	returns json language plpgsql as $$
		begin
			return (select json_agg(json_build_object(
				'id', "Book".id,
				'title', "Book".title,
				'author', "Book".author,
				'publisher', "Book".publisher
				)) from "Book" where "Book".author like concat('%', query, '%'));
		end;
	$$;

create function find_publisher(in query text)
	returns json language plpgsql as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Publisher".name,
				'telephone', "Publisher".telephone,
				'lastUpdate', "Publisher".lastUpdate
				)) from "Publisher" where "Publisher".name in (
					select publisher from "Book" where "Book".author LIKE concat('%', query, '%')
				)
			);
		end;
	$$;

create function delete_book_by_author(in auth text)
	returns void language plpgsql as $$
		begin 
			delete from "Book" where author = auth;
		end;
	$$;

create function delete_publisher_record(in id text)
	returns void language plpgsql as $$ 
		begin 
			delete from "Publisher" where name = id;
		end;
	$$;

create function delete_book_record(in id_ integer)
	returns void language plpgsql as $$
		begin 
			delete from "Book" where id = id_;
		end;
	$$;

create function update_publisher_by_name(in newname text, in id text)
	returns void language plpgsql as $$
		begin
			update "Publisher" set name = newname where name = id;
		end;
	$$;

create function update_publisher_by_tel(in newtel text, in id text)
	returns void language plpgsql as $$
		begin
			update "Publisher" set telephone = newtel where name = id;
		end;
	$$;

create function update_book_by_title(in newtitle text, in id_ integer)
	returns void language plpgsql as $$
		begin
			update "Book" set title = newtitle where id = id_;
		end;
	$$;

create function update_book_by_author(in newauthor text, in id_ integer)
	returns void language plpgsql as $$
		begin
			update "Book" set author = newauthor where id = id_;
		end;
	$$;

create function update_book_by_publisher(in newpublisher text, in id_ integer)
	returns void language plpgsql as $$
		begin
			update "Book" set publisher = newpublisher where id = id_;
		end;
	$$;
