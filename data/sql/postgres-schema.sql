--
-- Copyright (C) 2006 Async Open Source
--
-- This program is free software; you can redistribute it and/or
-- modify it under the terms of the GNU Lesser General Public License
-- as published by the Free Software Foundation; either version 2
-- of the License, or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU Lesser General Public License for more details.
--
-- You should have received a copy of the GNU Lesser General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
--
--
-- Author(s):       Evandro Vale Miquelito      <evandro@async.com.br>
--                  Johan Dahlin                <jdahlin@async.com.br>
--

--
-- Sequences
--

CREATE SEQUENCE stoqlib_abstract_bookentry_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_branch_identifier_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_branch_station_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_payment_identifier_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_purchase_ordernumber_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_purchasereceiving_number_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_sale_ordernumber_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

CREATE SEQUENCE stoqlib_sellable_code_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;

--
-- Table constraints
--

ALTER TABLE card_installment_settings ADD CONSTRAINT payment_day_check
      CHECK (payment_day <= 28);
ALTER TABLE card_installment_settings ADD CONSTRAINT closing_day_check
      CHECK (closing_day <= 28);
ALTER TABLE abstract_check_bill_adapter ADD CONSTRAINT monthly_interest_check
      CHECK (monthly_interest >= 0 AND monthly_interest <= 100);
ALTER TABLE abstract_check_bill_adapter ADD CONSTRAINT daily_penalty_check
      CHECK (daily_penalty >= 0 AND daily_penalty <= 100);
ALTER TABLE renegotiation_data ADD CONSTRAINT paid_check
      CHECK (paid_total >= 0);
